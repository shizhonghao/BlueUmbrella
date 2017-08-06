<template>
  <div class="logout" @keyup.enter="logout">
    <!-- <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
    </el-row> -->
    <el-card class="box-card">
      <el-row>
      </el-row>
      <!-- Navigate Row  -->
      <el-row>
        <el-col :span="6" :offset="4">
          <div>
            当前用户是: {{ current_user }}
          </div>
        </el-col>
        <el-col :span="6" :offset="6">
          <div>
            <el-button @click="logout" type="primary">Logout</el-button>
          </div>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'logout',
  computed: {
    current_user(){
      return sessionStorage.getItem("username")
    }
  },
  methods: {
    logout(){
      this.$ajax.get('/logout')
      .then( (response) => {
        sessionStorage.clear()
        this.$router.push('/login')
      })
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
  .box-card {
    margin: auto;
    width: 50%;
  }
</style>
