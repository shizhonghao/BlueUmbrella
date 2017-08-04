<template>
    <el-row type="flex" class="row-bg">
        <el-col :span="6" :offset="2">
            <div class="key">
                {{ key }}
            </div>
        </el-col>
        <el-col :span="4">
            <div class="val">
                {{ value }}
            </div>
        </el-col>
    </el-row>
</template>

<script>
export default {
    name: "InfoCol",
    data () {

    }

}
</script>

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



