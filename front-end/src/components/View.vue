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
      <el-tabs v-model="activeName" type="border-card" >
        <el-tab-pane label="用户信息" name="first">

          <el-row type="flex" class="row-bg">
            <el-col :span="4" offset="4">
              <div class="key">
                用户:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ current_user }}
              </div>
            </el-col>
          </el-row>


          <el-row type="flex" class="row-bg">
            <el-col :span="4" offset="4">
              <div class="key">
                ss密码:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ ss_password }}
              </div>
            </el-col>
          </el-row>


          <el-row type="flex" class="row-bg">
            <el-col :span="4" offset="4">
              <div class="key">
                enable:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ enable }}
              </div>
            </el-col>
          </el-row>


          <el-row type="flex" class="row-bg">

            <el-col :span="4" offset="4">
              <div class="key">
                protocol:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ protocol }}
              </div>
            </el-col>
          </el-row>


          <el-row type="flex" class="row-bg">
            <el-col :span="4" offset="4">
              <div class="key">
                method:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ method }}
              </div>
            </el-col>
          </el-row>


          <el-row type="flex" class="row-bg">

            <el-col :span="4" offset="4">
              <div class="key">
                obfs:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ obfs }}
              </div>
            </el-col>
            <el-row>
            </el-row>
          </el-row>


          <el-col :span="4" :offset="10">
            <el-button @click="$router.push('/logout')" type="primary">登出</el-button>
          </el-col>

        </el-tab-pane>


        <el-tab-pane label="SSR二维码" name="second">
          <vue-qr :bgSrc='src' :logoSrc="src2" text="这是一个测试界面" height="200" width="200"></vue-qr>
          <el-col :span="4" :offset="10">
            <el-button @click="$router.push('/logout')" type="primary">登出</el-button>
          </el-col>
        </el-tab-pane>

      </el-tabs>


    </div>
  </div>
</template>

<script>
  import VueQr from 'vue-qr'

  import ElCol from "element-ui/packages/col/src/col";
  export default {
    components: {ElCol,VueQr},
    name: 'view',
    data () {
      return {
        activeName: "first"
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
      },
      method(){
        return JSON.parse(sessionStorage.getItem("userinfo")).method
      },
      protocol(){
        return JSON.parse(sessionStorage.getItem("userinfo")).protocol
      },
      obfs(){
        return JSON.parse(sessionStorage.getItem("userinfo")).obfs
      },
      enable(){
        return JSON.parse(sessionStorage.getItem("userinfo")).enable
      },
      tableData(){
        return [{
          key:"username",
          value: "ray",
          description: "您的用户名"
        } , {
          key:"ss_password",
          value:"123",
          description: "您的shadowsocks密码"
        }
        ]
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
    margin-bottom: 10px;
  &:last-child {
     margin-bottom: 0;
   }
  }
  .el-col {
    border-radius: 4px;
  }
  .row-bg {
    padding: 5px 0;
    background-color: #f9fafc;
  }

  .text {
    font-size: 14px;
  }
  .item {
    padding: 18px 0;
  }
  .el-tabs {
    width: 480px;
    margin: auto;
  }
</style>
