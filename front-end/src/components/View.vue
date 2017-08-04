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
            <el-col :span="6" :offset="2">
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
            <el-col :span="6" :offset="2">
              <div class="key">
                邮箱:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ userinfo.email }}
              </div>
            </el-col>
          </el-row>

          <el-row type="flex" class="row-bg">
            <el-col :span="6" :offset="2">
              <div class="key">
                ss密码:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ userinfo.ss_password }}
              </div>
            </el-col>
          </el-row>


          <el-row type="flex" class="row-bg">
            <el-col :span="6" :offset="2">
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

            <el-col :span="6" :offset="2">
              <div class="key">
                协议:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ userinfo.protocol }}
              </div>
            </el-col>
          </el-row>


          <el-row type="flex" class="row-bg">
            <el-col :span="6" :offset="2">
              <div class="key">
                加密:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ userinfo.method }}
              </div>
            </el-col>
          </el-row>


          <el-row type="flex" class="row-bg">
            <el-col :span="6" :offset="2">
              <div class="key">
                混淆:&nbsp;
              </div>
            </el-col>
            <el-col :span="4">
              <div class="val">
                {{ userinfo.obfs }}
              </div>
            </el-col>
            <el-row>
            </el-row>
          </el-row>

          <el-row type="flex" class="row-bg">
            <el-col :span="6" :offset="2">
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
            <el-col :span="6" :offset="2">
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
            <el-col :span="6" :offset="2">
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
            <el-col :span="6" :offset="2">
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
          <vue-qr :text="text" size="400"></vue-qr>
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
  import URLSafeBase64 from 'urlsafe-base64'
  export default {
    components: {VueQr},
    name: 'view',
    data () {
      return {
        text:"ssr",
        activeName: "first",
        userinfo: {
          email: "",
          ss_password: "",
          port: 0,
          method : "",
          protocol: "",
          obfs: "",
          enable: "",
          upward_transfer: 0,
          downward_transfer: 0,
          transfer_enable: 0
        }
      }
    },
    computed:{
      current_user(){
        return sessionStorage.getItem("username")
      },
      enable(){
        if(this.userinfo.enable){
          return "可用"
        } else {
          return "不可用"
        }

      },
      upward_transfer(){
        return dataflow_convert(this.userinfo.upward_transfer)
      },
      downward_transfer(){
        return dataflow_convert(this.userinfo.downward_transfer)
      },
      transfer_enable(){
        return dataflow_convert(this.userinfo.transfer_enable)
      },
      transfer_remain(){
          var remain = this.userinfo.transfer_enable
            - this.userinfo.upward_transfer
            - this.userinfo.downward_transfer
        return dataflow_convert(remain)
      },
      ssr_link(){

        var dict = this.userinfo
        var encoded_password = URLSafeBase64.encode(Buffer(dict.ss_password))
        var link = "172.104.106.82:" + dict.port + ":" + dict.protocol.replace("_compatible", "")
            + ":" + dict.method + ":" + dict.obfs.replace("_compatible", "") + ":" + encoded_password
        var encoded_link = URLSafeBase64.encode(Buffer(link))
        encoded_link.replace('/=/g', '')
        this.text = "ssr://" + encoded_link
        return "ssr://" + link
      }
    },
    methods: {
    },
    beforeCreate(){
      if(!(sessionStorage.getItem("state") && JSON.parse(sessionStorage.getItem("state")))){
        this.$router.push('/login')
      } else {
        this.$ajax.get('/users/'.concat(sessionStorage.getItem("username")))
        .then((response) => {
          this.userinfo = response.data
          console.log(this.userinfo)
        })
        .catch((error) =>{
          console.log(error)
        })
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
