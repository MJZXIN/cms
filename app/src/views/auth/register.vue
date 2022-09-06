<template>
  <el-form
    ref="ruleFormRef"
    :model="ruleForm"
    status-icon
    :rules="rules"
    label-width="120px"
    class="demo-ruleForm"
  >
    <el-form-item label="用户名：" prop="username">
      <el-input v-model="ruleForm.username" type="text" autocomplete="off" />
    </el-form-item>
    <el-form-item label="密码：" prop="password">
      <el-input
        v-model="ruleForm.password"
        type="passwordword"
        autocomplete="off"
      />
    </el-form-item>
    <el-form-item label="确认密码：" prop="checkpassword">
      <el-input
        v-model="ruleForm.checkpassword"
        type="passwordword"
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
import useCurrentInstance from "@/utils/getCurrentInstance";
import { register } from "../../api/index";
import router from "../../router/index";

const { proxy } = useCurrentInstance();

const ruleFormRef = ref<FormInstance>();

const validateusernamename = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("用户名不能为空"));
  } else if (value === " ") {
    callback(new Error("用户名不能为空格"));
  } else {
    callback();
  }
};

const validatepassword = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("请输入密码"));
  } else {
    if (ruleForm.checkpassword !== "") {
      if (!ruleFormRef.value) return;
      ruleFormRef.value.validateField("checkpassword", () => null);
    }
    callback();
  }
};

const validatepassword2 = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("请再次输入密码"));
  } else if (value !== ruleForm.password) {
    callback(new Error("两次输入的密码不相同"));
  } else {
    callback();
  }
};

const ruleForm = reactive({
  username: "",
  password: "",
  checkpassword: "",
});

const rules = reactive({
  username: [{ validator: validateusernamename, trigger: "blur" }],
  password: [{ validator: validatepassword, trigger: "blur" }],
  checkpassword: [{ validator: validatepassword2, trigger: "blur" }],
});

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.validate((valid) => {
    if (valid) {
      register(ruleForm)
        .then((res) => {
          proxy.$message.success(res.msg);
          router.push("/login");
        })
        .catch(() => {
          proxy.$message.error("网络异常,请检查网络");
        });
    } else {
      proxy.$message.error("请检查注册信息是否正确");
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
