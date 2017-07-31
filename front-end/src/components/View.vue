<template>
  <div class="view">
    <!-- <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
    </el-row> -->
    <el-row>
    </el-row>
    <!-- Navigation Row  -->
    <el-row>
      <el-col :span="6" :offset="4">
        <div>
          当前用户是: {{ current_user }}
        </div>
      </el-col>
      <el-col :span="2" :offset="6">
        <el-button @click="$router.push('/logout')" type="primary">登出</el-button>
      </el-col>
    </el-row>
    
    <!-- Row for datas (prototype)  -->
    <el-row>
      <el-col :span="4" :offset="7">
        <div>
          Username:
        </div>
      </el-col>
      <el-col :span="4" :offset="1">
        <div>
          Ray
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'view',
  data () {
    return {
      username: this.$username,
      password: ''
    }
  },
  computed:{
    current_user (){
      return localStorage.getItem("username")
    }
  },
  methods: {
    login_req() {
      this.username = this.$username
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
