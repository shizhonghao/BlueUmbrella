<template>
  <div class="register">
    <!-- <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
    </el-row> -->
    <el-row>
      <el-col :span="4" :offset="10">
        <div>
          <el-input v-model="username" placeholder="Username"></el-input>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="4" :offset="10">
        <div>
          <el-input v-model="password" placeholder="Password"></el-input>
        </div>
      </el-col>
    </el-row>
      <el-row>
      <el-col :span="4" :offset="10">
        <div>
          <el-input v-model="email" placeholder="Email address"></el-input>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="2" :offset="10">
        <div>
          <el-button type="primary" @click="register">注册</el-button>
        </div>
      </el-col>
      <el-col :span="2">
        <div>
          <el-button type="primary" @click="$router.push('/login')">返回</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'register',
  data () {
    return {
      username: '',
      password: '',
      email: ''
    }
  },
  methods: {
    register() {
      if(this.username == "" || this.password == ""){
        this.$message.error('请先输入用户名和密码')
        //Will be overridden later
      } else {
        this.$ajax.post('/register', {
          username: this.username,
          password: this.password,
          email: this.email
        })
        .then((response) => {
          sessionStorage.setItem("state", true)
          sessionStorage.setItem("username", response.data.CurrentUser)
          this.$router.push('/view')
        })
        .catch((error) => {
          if(error.response){
            if(error.response.status == 500){
              this.$message.error(error.response.data.message)
            } else {
              console.log(error)
            }
          } else {
            console.log(error)
          }
        })
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .grid-content {
    border-radius: 4px;
    min-height: 34px;
  }
  .bg-purple {
    background: #d3dce4;
  }
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f10fafc;
  }
</style>
