<template>
  <el-form
    ref="formRef"
    :model="formData"
    :rules="rules"
    status-icon
    class="demo-ruleForm"
  >
    <el-form-item label="用户名：" prop="username">
      <el-input v-model="formData.username" type="text" autocomplete="off" />
    </el-form-item>
    <el-form-item label="密码：" prop="password">
      <el-input
        v-model="formData.password"
        type="passwordwod"
        autocomplete="off"
      />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm(formRef)">登录</el-button>
      <el-button @click="goRegister">注册</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive, ref } from "vue";
import type { FormInstance } from "element-plus";
import useCurrentInstance from "@/utils/getCurrentInstance";
import router from "../../router";
import { login } from "api/index";
import { setUserInfo } from "utils/user";

const { proxy } = useCurrentInstance();
const formRef = ref<FormInstance>();

const formData = reactive({
  username: "SYSTEM",
  password: "123456",
});

const checkusername = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("请输入用户名"));
  }
  return callback();
};

const checkpassword = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("请输入密码"));
  }
  return callback();
};

const rules = reactive({
  username: [{ validator: checkusername, trigger: "blur" }],
  password: [{ validator: checkpassword, trigger: "blur" }],
});

localStorage.removeItem("USER_INFO");

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.validate((valid) => {
    if (valid) {
      // console.log(proxy);
      console.log(formData);
      login(formData)
        .then((res) => {
          // token.$patch((state) => {
          //   state.token = "Bearer " + res.data.token;
          // });
          // token.user.setUserInfo(res.data.userinfo);
          setUserInfo(res.data);
          if (res.code) {
            proxy.$message.success(res.msg);
          } else {
            proxy.$message.error(res.msg);
          }
          router.replace("/");
        })
        .catch(() => {
          proxy.$message.error("网络异常,请检查网络");
        });
    } else {
      proxy.$message.error("请检查登录信息是否正确");
      return false;
    }
  });
};

const goRegister = () => {
  router.push("/register");
};
</script>

<style scoped></style>
