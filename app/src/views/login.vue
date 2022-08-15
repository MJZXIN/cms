<template>
  <div>
    <el-form>dd</el-form>
    <button type="button" @click="admin">dd</button>
  </div>
</template>

<script>
import { getCurrentInstance } from 'vue'
import { ElMessage } from 'element-plus'
export default {
  setup() {
    const { proxy } = getCurrentInstance()
    function admin() {
      console.log(12)
      // ElMessage.success({
      //   "showClose": true,
      //   "message": "登录成功"
      // })
      proxy.$message.success('---')
    }
    return {
      admin
    }
  }
}
</script>
<style scoped>
</style>