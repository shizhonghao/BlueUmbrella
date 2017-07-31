<template>
  <div class="login">
    <!-- <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
    </el-row> -->
    <el-row>
    </el-row>
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
    </el-row>
    <el-row>
      <el-col :span="2" :offset="10">
        <div>
          <el-button type="primary" @click="$router.push('/register')">注册</el-button>
        </div>
      </el-col>
      <el-col :span="2">
        <div>
          <el-button type="primary" @click="login">登录</el-button>
        </div>
      </el-col>
    </el-row>
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
        alert('INPUT YOUR INFO FIRST')
        //Will be overridden later
      } else {
        this.$ajax.post('/login', {
          username: this.username,
          password: this.password
        })
        .then((response) => {
          if(response.status == 200){
            // Logged in
            localStorage.setItem("state", true)
            localStorage.setItem("username", response.data.CurrentUser)
            this.$router.push('/view')
          } else {
            alert('NOT MATCH!')
          }
        })
        .catch((error) => {
          console.log(error)
          alert('NOT MATCH!')
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
    min-height: 36px;
  }
  .bg-purple {
    background: #d3dce6;
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
    background-color: #f9fafc;
  }
</style>
