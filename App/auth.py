from flask import Blueprint, jsonify, request, current_app
from flask_login import LoginManager, login_user, current_user, logout_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import check_password_hash, generate_password_hash
from App.config import SECRET_KEY, EXPIRATION
from functools import wraps


auth = Blueprint('auth', __name__)
login_manager = LoginManager()

@login_manager.user_loader
def user_loader(user_id):
    from App.models import User
    return User.objects(id=user_id).first()

# Customized login method (by token)
@login_manager.request_loader
def request_loader(request):
    token = request.headers.get('Authentication')
    if not token:
        token = request.args.get('Token')    
    if token:
        from App.models import User
        s = Serializer(SECRET_KEY, expires_in=EXPIRATION)
        user=s.loads(token).get('username')
        return User.objects(username=user).first()
    return None


@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        from App.models import User
        req = request.get_json()
        if not req:
            raise APIException("Bad Request", "Request should be json", 400)
        if not (req.get('username') and req.get('password')):
            raise APIException("Bad Request", "Need username and password", 400)
        user = User.objects(username=req['username']).first()
        if user and check_password_hash(user.password, req['password']):
            login_user(user, remember=True)
            return jsonify(CurrentUser=current_user.username, Token=get_token(user)) 
        else:
            raise APIException("Wrong Info", "Wrong username or password!", 500)
    if request.method == "GET":
        if current_user.is_authenticated:
            #just for debugging here
            return jsonify(LoggedIn=True, CurrentUser=current_user.username)
        else:
            return jsonify(LoggedIn=False)
            

@auth.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return jsonify(Success=True)

@auth.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        if current_user.is_authenticated:
            raise APIException("Wrong Status", "You have already logged in!", 500)
        from App.models import User, SSUsers
        req = request.get_json()
        if not req:
            raise APIException("Bad Request", "Request should be json", 400)
        if not (req.get('username') and req.get('password')):
            raise APIException("Bad Request", "Need username and password", 400)
        #Try if the username is existed
        new = User.objects(username=req.get('username'))
        if new:
            raise APIException("Internal Error", "Existed user!", 500)
        new = User(username = req.get('username'), \
                    password = generate_password_hash(req.get('password')), \
                    #if email does not exist in the request, set it as null string
                    email = req.get('email',""), \
                    is_active = True,\
                    is_admin = False)
        new.save()
        SSUsers().add(req.get('username'), req.get('password'))
        login_user(new, remember=True)
        return jsonify(CurrentUser=current_user.username, Token=get_token(new))
    



def get_token(user):
    s = Serializer(SECRET_KEY, expires_in=EXPIRATION)
    return s.dumps({"username":user.username}).decode('utf-8')


# A common type of error handler, may be refined later
class APIException(Exception):
    def __init__(self, error_id, message, code=500):
        super(Exception, self).__init__()
        self.raw_message = message
        self.error_id = error_id
        self.code = code
        self.message = message

    def to_dict(self):
        result = {
            "id": self.error_id,
            "code": self.code,
            "message": self.message,
        }
        return result

# 401 Error, follows the template of APIException
@login_manager.unauthorized_handler
def unauthorized_handler():
    response = jsonify({"id":"Unauthorized", "code":401, "message":"You may need to login or you don't have the permission"})
    response.status_code = 401
    return response

# Catch the exception and return the jsonified data with status code
@auth.errorhandler(APIException)
def handle_api_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.code 
    return response

# A decorator for requiring admin permission
def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_admin:
            return current_app.login_manager.unauthorized()
        return f(*args, **kwargs)
    return decorated

# # Overrided wrapper for supporting permission contro
# def login_required(admin=False):
#     def wrapper(fn):
#         @wraps(fn)
#         def decorated_view(*args, **kwargs):
#             if not current_user.is_authenticated:
#                 return current_app.login_manager.unauthorized()
#             if admin == True and (not current_user.is_admin):
#                 return current_app.login_manager.unauthorized()
#             return fn(*args, **kwargs)
#         return decorated_view
#     return wrapper
