<template>
  <div><h1>看板界面</h1></div>
  <div>
    <el-button @click="req()" autoInsertSpace>Token</el-button>
    <div>{{ Token }}</div>
  </div>
  <div><el-button @click="Info" autoInsertSpace>用户信息</el-button></div>
  <div>{{ userInfo }}</div>
  <div><el-button @click="route">路由</el-button></div>
  <div>{{ Routes }}</div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { userStore } from "@/store/modules/user";

const user = userStore();

let userInfo = ref(null);
let Routes = ref(null);
let Token = ref(null);

const Info = () => {
  console.log(user);
  userInfo.value = user.$state.userInfo;
  console.log(user.$state.userInfo);
};

const route = () => {
  console.log(user);
  Routes.value = user.$state.routes;
  console.log(user.$state.routes);
};

const req = () => {
  console.log(user.$state.token);
  console.log(user.$state.userInfo);
  console.log(user.$state.routes);
  Token.value = user.token;
};
</script>

<style scoped></style>
