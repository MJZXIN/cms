<template>
  <el-form ref="formRef" :model="formData" :rules="rules" status-icon class="demo-ruleForm">
    <el-form-item label="用户名：" prop="user">
      <el-input v-model="formData.user" type="text" autocomplete="off" />
    </el-form-item>
    <el-form-item label="密码：" prop="pass">
      <el-input v-model="formData.pass" type="passwod" autocomplete="off" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm(formRef)">登录</el-button>
      <el-button @click="goRegister">注册</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormInstance } from 'element-plus'
import useCurrentInstance from '@/utils/getCurrentInstance';
import router from '@/router/index'
const { proxy } = useCurrentInstance()
const formRef = ref<FormInstance>()

const formData = reactive({
  user: "",
  pass: ""
})

const checkUser = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error("请输入用户名"))
  }
  return callback()
}

const checkPass = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error("请输入密码"))
  }
  return callback()
}

const rules = reactive({
  user: [{ validator: checkUser, trigger: 'blur' }],
  pass: [{ validator: checkPass, trigger: 'blur' }]
})

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      console.log("submit!")
      console.log(proxy)
      proxy.$message.success("登录成功")
    } else {
      console.log("error submit!")
      return false
    }
  })
}

const goRegister = () => {
  console.log("sjkdhglkjdshgkjgh")
  router.push("/register")
}
</script>

<style scoped>
</style>