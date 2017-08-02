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
                邮箱:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ e_mail }}
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
                可用性:&nbsp;
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
                协议:&nbsp;
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
                加密:&nbsp;
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
                混淆:&nbsp;
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

          <el-row type="flex" class="row-bg">
            <el-col :span="4" offset="4">
              <div class="key">
                上传流量:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ upward_transfer }}
              </div>
            </el-col>
            <el-row>
            </el-row>
          </el-row>

          <el-row type="flex" class="row-bg">
            <el-col :span="4" offset="4">
              <div class="key">
                下载流量:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ downward_transfer }}
              </div>
            </el-col>
            <el-row>
            </el-row>
          </el-row>

          <el-row type="flex" class="row-bg">
            <el-col :span="4" offset="4">
              <div class="key">
                总流量:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ transfer_enable }}
              </div>
            </el-col>
            <el-row>
            </el-row>
          </el-row>

          <el-row type="flex" class="row-bg">
            <el-col :span="4" offset="4">
              <div class="key">
                剩余流量:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ transfer_remain }}
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
          <el-col>
            也可通过扫描二维码录入信息
            {{ ssr_link }}
          </el-col>
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
  function dataflow_convert(dat){
    if(dat<1024)
    {
        return dat+"B"
    }
    else if(dat<1048576)
    {
      var x = dat/1024
      return x.toFixed(2)+"KB"
    }
    else if(dat<1073741824)
    {
      var x = dat/1048576
      return x.toFixed(2)+"MB"
    }
    else
    {
      var x = dat/1073741824
      return x.toFixed(2)+"GB"
    }
    return dat
  }

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
      e_mail(){
        return JSON.parse(sessionStorage.getItem("userinfo")).e_mail
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
      upward_transfer(){
        return dataflow_convert(JSON.parse(sessionStorage.getItem("userinfo")).upward_transfer)
      },
      downward_transfer(){
        return dataflow_convert(JSON.parse(sessionStorage.getItem("userinfo")).downward_transfer)
      },
      transfer_enable(){
        return dataflow_convert(JSON.parse(sessionStorage.getItem("userinfo")).transfer_enable)
      },
      transfer_remain(){
          var remain = JSON.parse(sessionStorage.getItem("userinfo")).transfer_enable
            - JSON.parse(sessionStorage.getItem("userinfo")).upward_transfer
            - JSON.parse(sessionStorage.getItem("userinfo")).downward_transfer
        return dataflow_convert(remain)
      },
      ssr_link(){
        var URLSafeBase64 = require('urlsafe-base64');
        var dict = JSON.parse(sessionStorage.getItem("userinfo"))
        //var buf = new Buffer(dict.password)
          var link = "tbufoundation.tk:" + dict.port + ":" + dict.protocol.replace("_compatible", "")
            + ":" + dict.method + ":" + dict.obfs.replace("_compatible", "") + ":"
            //+ buf
          return "ssr://" + link
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
    text-align:left;
    font-size: 1em;
    font-style: italic;
    font-weight: 600;
    margin-top: 0px;
    padding: 0;
  }
  .val{
    text-align:left;
    font-size: 1em;
    /*font-style: italic;*/
    /*font-weight: 100;*/
    margin-top: 0px;
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
