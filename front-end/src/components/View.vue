<template>
  <div class="view">
    <!-- <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
    </el-row> -->

    <div class="item">

      <!--<el-col v-for="key in users">
        <div class="key">
          {{ key }} ,{{ val }}:&nbsp;
        </div>
      </el-col>-->

      <el-col :span="4" :offset="8" >
        <div class="key">
          用户:&nbsp;
        </div>
      </el-col>
      <el-col :span="4" :offset="0" >
        <div class="val">
          {{ current_user }}
        </div>
      </el-col>
      <el-row>
      </el-row>

      <el-col :span="4" :offset="8" >
        <div class="key">
          ss密码:&nbsp;
        </div>
      </el-col>
      <el-col :span="4" :offset="0" >
        <div class="val">
          {{ ss_password }}
        </div>
      </el-col>
      <el-row>
      </el-row>

      <el-col :span="4" :offset="8" >
        <div class="key">
          port:&nbsp;
        </div>
      </el-col>
      <el-col :span="4" :offset="0" >
        <div class="val">
          {{ port }}
        </div>
      </el-col>
      <el-row>
      </el-row>


      <el-col :span="4" :offset="10">
        <el-button @click="$router.push('/logout')" type="primary">登出</el-button>
      </el-col>

    </div>
  </div>
</template>

<script>

  import ElCol from "element-ui/packages/col/src/col";
export default {
  components: {ElCol},
  name: 'view',
  data () {
    return {
    }
  },
  computed:{
    current_user(){
      return sessionStorage.getItem("username")
    },
    ss_password(){
        return JSON.parse(sessionStorage.getItem("userinfo")).ss_password
    },
    port(){
      return JSON.parse(sessionStorage.getItem("userinfo")).port
    }
  },
  methods: {
  },
  beforeCreate(){
    if(!(sessionStorage.getItem("state") && JSON.parse(sessionStorage.getItem("state")))){
      this.$router.push('/login')
    }
  }
} 
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .item{
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .key{
    text-align:right;
    font-size: 1em;
    font-style: italic;
    font-weight: 600;
    margin-top: 16px;
    padding: 0;
  }
  .val{
    text-align:left;
    font-size: 1em;
    /*font-style: italic;*/
    /*font-weight: 100;*/
    margin-top: 16px;
    padding: 0;
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
