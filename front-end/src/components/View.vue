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

          <infoCol
          keyword="用户: "
          :value="current_user">
          </infoCol>

          <infoCol
          keyword="邮箱: "
          :value="userinfo.email">
          </infoCol>

          <infoCol
          keyword="端口: "
          :value="userinfo.port.toString()">
          </infoCol>

          <infoCol
          keyword="ss密码: "
          :value="userinfo.ss_password"
          :tooltip="true"
          description="此密码用于填写Shadowsocks密码 <br/> 建议将其修改为与登陆密码不一致">
          </infoCol>

          <infoCol
          keyword="可用性: "
          :value="enable"
          :tooltip="true"
          description="请联系管理员修改为可用">
          </infoCol>

          <infoCol
          keyword="协议: "
          :value="userinfo.protocol">
          </infoCol>

          <infoCol
          keyword="加密: "
          :value="userinfo.method">
          </infoCol>

          <infoCol
          keyword="混淆: "
          :value="userinfo.obfs">
          </infoCol>

          <infoCol
          keyword="上传流量: "
          :value="upward_transfer">
          </infoCol>

          <infoCol
          keyword="下载流量: "
          :value="downward_transfer">
          </infoCol>

          <infoCol
          keyword="总流量: "
          :value="transfer_enable">
          </infoCol>

          <infoCol
          keyword="剩余流量: "
          :value="transfer_remain">
          </infoCol>

          <br/>

          <el-col :span="4" :offset="6">
            <el-button @click="$router.push('/edit')" type="primary">修改</el-button>
          </el-col>
          <el-col :span="4" :offset="4">
            <el-button @click="$router.push('/logout')" type="primary">登出</el-button>
          </el-col>

        </el-tab-pane>


        <el-tab-pane label="SSR二维码" name="second">
          <el-col>
            也可通过扫描二维码录入信息
            {{ ssr_link }}
          </el-col>
          <vue-qr :text="text" :logoSrc="logo" size="400" :logoScale="0.4"></vue-qr>
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
    return dat.toString()
  }

  import VueQr from 'vue-qr'
  import URLSafeBase64 from 'urlsafe-base64'
  import infoCol from './InfoCol.vue'
  export default {
    components: {VueQr, infoCol},
    name: 'view',
    data () {
      return {
        text:"ssr",
        activeName: "first",
        logo: require('@/assets/TBU.jpg'),
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
        },
        keytable: {
          test: "Test"
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
    created(){
      if(!(sessionStorage.getItem("state") && JSON.parse(sessionStorage.getItem("state")))){
        this.$router.push('/login')
      } else {
        this.$ajax.get('/users/'.concat(sessionStorage.getItem("username")))
        .then((response) => {
          this.userinfo = response.data
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
  .el-row {
    margin-bottom: 10px;
  }
  .el-row:last-child {
     margin-bottom: 0;
  }
  .el-col {
    border-radius: 4px;
  }
  .row-bg {
    padding: 5px 0;
    background-color: #f9fafc;
  }
  .item {
    padding: 18px 0;
  }
  .el-tabs {
    width: 480px;
    margin: auto;
  }
</style>
