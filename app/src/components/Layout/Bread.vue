<template>
  <el-breadcrumb separator="/">
    <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
    <el-breadcrumb-item><a href="/">**管理</a></el-breadcrumb-item>
    <el-breadcrumb-item>{{ this.$route.meta.title }}</el-breadcrumb-item>
  </el-breadcrumb>
</template>

<script>
// import { Menu as IconMenu, Setting } from "@element-plus/icons-vue";
import router from "@/router";
import { userStore } from "@/store/modules/user";
import { appStore } from "store/modules/app";

export default {
  name: "Bread",
};
</script>

<style scoped></style>
