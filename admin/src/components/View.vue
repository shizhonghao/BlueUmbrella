<template>
  <div class="view">
    <el-table :data="tableData" border style="width:100%">
      <el-table-column label="用户名">
        <template scope="scope">
          <el-popover trigger="hover" placement="top">
            <p> 端口: {{scope.row.port}} </p>
            <p> SS密码: {{scope.row.ss_password}} </p>
            <p> 协议: {{scope.row.protocol}} </p>
            <p> 加密: {{scope.row.method}} </p>
            <p> 混淆: {{scope.row.obfs}} </p>
            <p> 上传流量: {{scope.row.upward_transfer}} </p>
            <p> 下载流量: {{scope.row.downward_transfer}} </p>
            <p> 总流量: {{scope.row.transfer_enable}} </p>
            <p> 剩余流量: {{scope.row.transfer_remain}} </p>
            <div slot="reference" class="name-wrapper">
              <el-tag> {{scope.row.username}} </el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column label="邮箱" prop="email">
      </el-table-column>
      <el-table-column label="可用性">
        <template scope="scope">
          <div>
            {{scope.row.enable}}
          </div>
          <el-button size="small">更改</el-button>
        </template>
      </el-table-column>
    </el-table>
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

  import URLSafeBase64 from 'urlsafe-base64'
  export default {
    name: 'view',
    data () {
      return {
        userinfo: {}
      }
    },
    computed: {
      tableData(){
        var savedData = new Array
        for(var singleUser in this.userinfo){
          var tmp = JSON.parse(JSON.stringify(this.userinfo[singleUser]))
          tmp.username=singleUser
          tmp.enable = tmp.enable ? "可用" : "不可用"
          var remain= tmp.transfer_enable - tmp.upward_transfer - tmp.downward_transfer
          tmp.upward_transfer = dataflow_convert(tmp.upward_transfer)
          tmp.downward_transfer = dataflow_convert(tmp.downward_transfer)
          tmp.transfer_enable = dataflow_convert(tmp.transfer_enable)
          tmp.transfer_remain = dataflow_convert(remain)
          savedData.push(tmp)
        }
        return savedData
      },
      current_user(){
        return sessionStorage.getItem("username")
      }
    },
    methods: {
    },
    created(){
      if(!(sessionStorage.getItem("state") && JSON.parse(sessionStorage.getItem("state")))){
        this.$router.push('/login')
      } else {
        this.$ajax.get('/users')
        .then((response) => {
          this.userinfo = response.data
          console.log(this.userinfo)
        })
        .catch((error) => {
          if(error.response){
            if(error.response.status == 401){
              this.$message.error("权限错误!")
              this.$router.push('/login')
            } else {
              console.log(error)
            }
          } else {
            console.log(error)
          }
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
