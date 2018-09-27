<template>
  <div class="login" @keyup.enter="login">
    <!-- <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
    </el-row> -->
    <el-card class="box-card">
      <el-row>
      </el-row>
      <el-row>
        <el-col :span="10" :offset="7">
          <div>
            <el-input
            v-model="username"
            placeholder="用户名"
            required>
            </el-input>
          </div>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="10" :offset="7">
          <div>
            <el-input
            v-model="password"
            placeholder="密码"
            type="password"
            required>
            </el-input>
          </div>
        </el-col>
      </el-row>
      <el-row>
      </el-row>
      <el-row>
        <el-col :span="2" :offset="4">
          <div>
            <el-button type="primary" @click="login">登录</el-button>
          </div>
        </el-col>
      </el-row>

    </el-card>
  </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login() {
      if(this.username == "" || this.password == ""){
        this.$message.error('请先输入用户名和密码')
        //Will be overridden later
      } else {
        this.$ajax.post('/login', {
          username: this.username,
          password: this.password
        })
        .then((response) => {
          // Logged in
          sessionStorage.setItem("state", true)
          sessionStorage.setItem("username", response.data.CurrentUser)
          this.$router.push('/view')
        })
        .catch((error) => {
          if(error.response.status == 500){
            this.$message.error('用户名或密码不正确！')
          } else {
            console.log(error)
          }
        })
      }
    }
  },
  created(){
    if(JSON.parse(sessionStorage.getItem("state"))){
      this.$router.push('/view')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .el-row {
    margin-bottom: 20px;
  }
  .el-row:last-child {
      margin-bottom: 0;
  }
  .el-col {
    border-radius: 4px;
  }
  .box-card {
    margin: auto;
    width: 360px;
  }
</style>
