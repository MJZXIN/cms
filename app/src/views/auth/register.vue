<template>
  <el-form
    ref="ruleFormRef"
    :model="ruleForm"
    status-icon
    :rules="rules"
    label-width="120px"
    class="demo-ruleForm"
  >
    <el-form-item label="用户名：" prop="user">
      <el-input v-model="ruleForm.user" type="text" autocomplete="off" />
    </el-form-item>
    <el-form-item label="密码：" prop="pass">
      <el-input v-model="ruleForm.pass" type="password" autocomplete="off" />
    </el-form-item>
    <el-form-item label="确认密码：" prop="checkPass">
      <el-input
        v-model="ruleForm.checkPass"
        type="password"
        autocomplete="off"
      />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm(ruleFormRef)"
        >注册</el-button
      >
      <el-button @click="goLogin">返回登录</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive, ref } from "vue";
import type { FormInstance } from "element-plus";
import { rule } from "postcss";
import useCurrentInstance from "../../utils/getCurrentInstance";
import { registry } from "../../api/index";
import router from "../../router/index";
import { ElMessage } from "element-plus";

const ruleFormRef = ref<FormInstance>();

const validateUsername = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("用户名不能为空"));
  } else if (value === " ") {
    callback(new Error("用户名不能为空格"));
  } else {
    callback();
  }
};

const validatePass = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("请输入密码"));
  } else {
    if (ruleForm.checkPass !== "") {
      if (!ruleFormRef.value) return;
      ruleFormRef.value.validateField("checkPass", () => null);
    }
    callback();
  }
};

const validatePass2 = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("请再次输入密码"));
  } else if (value !== ruleForm.pass) {
    callback(new Error("两次输入的密码不相同"));
  } else {
    callback();
  }
};

const ruleForm = reactive({
  user: "",
  pass: "",
  checkPass: "",
});

const rules = reactive({
  user: [{ validator: validateUsername, trigger: "blur" }],
  pass: [{ validator: validatePass, trigger: "blur" }],
  checkPass: [{ validator: validatePass2, trigger: "blur" }],
});
const { proxy } = useCurrentInstance();
const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.validate((valid) => {
    if (valid) {
      console.log("submit!");
      // registry(ruleForm);
      setTimeout(() => {
        console.log(proxy);
        // ElMessage.success("sd")
        // useCurrentInstance.$message.success("0000")
      }, 1000);
    } else {
      console.log("error submit!");
      return false;
    }
  });
};

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.resetFields();
};

const goLogin = () => {
  router.push("/login");
};
</script>
