<template>
  <div class="edit">
    <!-- <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
    </el-row> -->

    <el-form ref="form" :model="form" label-width="80px">

      <el-form-item label="加密">
        <el-select v-model="form.method" placeholder="请选择加密方式（method）">
          <el-option label="none" value="none"></el-option>
          <el-option label="aes-128-cfb" value="aes-128-cfb"></el-option>
          <el-option label="aes-192-cfb" value="aes-192-cfb"></el-option>
          <el-option label="aes-256-cfb" value="aes-256-cfb"></el-option>
          <el-option label="rc4-md5" value="rc4-md5"></el-option>
          <el-option label="rc4-md5-6" value="rc4-md5-6"></el-option>
          <el-option label="chacha20" value="chacha20"></el-option>
          <el-option label="chacha20-ietf" value="chacha20-ietf"></el-option>
          <el-option label="salsa20" value="salsa20"></el-option>
          <el-option label="aes-128-ctr" value="aes-128-ctr"></el-option>
          <el-option label="aes-192-ctr" value="aes-192-ctr"></el-option>
          <el-option label="aes-256-ctr" value="aes-256-ctr"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="协议">
        <el-select v-model="form.protocol" placeholder="请选择协议（protocol）">
          <el-option label="origin" value="origin"></el-option>
          <el-option label="auth_sha1_v4" value="auth_sha1_v4"></el-option>
          <el-option label="auth_sha1_v4_compatible" value="auth_sha1_v4_compatible"></el-option>
          <el-option label="auth_aes128_md5" value="auth_aes128_md5"></el-option>
          <el-option label="auth_aes128_sha1" value="auth_aes128_sha1"></el-option>
          <el-option label="auth_chain_a" value="auth_chain_a"></el-option>
        </el-select>
      </el-form-item>


      <el-form-item label="混淆">
        <el-select v-model="form.obfs" placeholder="请选择混淆方式（OBFS）">
          <el-option label="plain" value="plain"></el-option>
          <el-option label="http_simple_compatible" value="http_simple_compatible"></el-option>
          <el-option label="http_simple" value="http_simple"></el-option>
          <el-option label="tls1.2_ticket_auth_compatible" value="tls1.2_ticket_auth_compatible"></el-option>
          <el-option label="tls1.2_ticket_auth" value="tls1.2_ticket_auth"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="e-mail">
        <el-input v-model="form.email"></el-input>
      </el-form-item>

      <el-form-item label="ss密码">
        <el-input v-model="form.ss_password"></el-input>
      </el-form-item>

      <el-form-item label="密码">
        <el-input v-model="form.password"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>


  </div>
</template>

<script>
export default {
  name: 'edit',
  data () {
    return {
      form: {
        email: '',
        ss_password:'',
        password:'',
        method: '',
        protocol: '',
        obfs: '',
      }
    }
  },
  methods: {
    login_req() {
      return true
    },
    onSubmit() {
      console.log('submit!');
    }
  },
  created(){
    this.form.email = JSON.parse(sessionStorage.getItem("userinfo")).email
    this.form.ss_password = JSON.parse(sessionStorage.getItem("userinfo")).ss_password
    this.form.obfs = JSON.parse(sessionStorage.getItem("userinfo")).obfs
    this.form.method = JSON.parse(sessionStorage.getItem("userinfo")).method
    this.form.protocol = JSON.parse(sessionStorage.getItem("userinfo")).protocol
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
  .el-form{
    border: 1px solid #eaeefb;
    border-radius: 4px;
    transition: all 0.2s ease 0s;
    padding: 24px;
    width: 480px;
    margin: auto;
  }
  .el-option{
    width: 240px;
  }
</style>
