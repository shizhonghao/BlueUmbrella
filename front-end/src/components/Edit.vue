<template>
  <div class="edit">
    <!-- <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
    </el-row> -->
    <el-row>
      <el-col :span="6" :offset="9">
        <div>
          Username: <el-input v-model="username" placeholder="Should be here"></el-input>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6" :offset="9">
        <div>
          Password: <el-input v-model="password" placeholder="Should be here"></el-input>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6" :offset="9">
        <div>
          <el-button type="primary">EDIT</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'edit',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login_req() {
      return true
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
