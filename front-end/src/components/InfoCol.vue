<template>
  <el-tooltip :disabled="! tooltip" placement="left">
    <div slot="content" v-html="description"></div>
    <el-row type="flex" class="row-bg">
        <el-col :span="keyspan" :offset="offset">
            <div class="key">
                {{ keyword }}
            </div>
        </el-col>
        <el-col :span="valuespan">
            <div class="val">
                {{ value }}
                <slot></slot>
            </div>
        </el-col>
    </el-row>
  </el-tooltip>
</template>

<script>
export default {
    name: "infoCol",
    props: {
      keyword : String,
      value: String,
      description: String,
      secondLine: {
        type: String,
        default: ""
      },
      keyspan: {
        type: Number,
        default: 6
      },
      valuespan:{
        type: Number,
        default: 4
      },
      offset: {
        type: Number,
        default: 2
      },
      tooltip:{
        type: Boolean,
        default: false
      }
    }
}
</script>

<style scoped>
  .key{
    text-align:left;
  }
  .val{
    text-align:left;
  }
  .row-bg {
    background-color: #f9fafc;
  }
</style>



