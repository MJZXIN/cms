<template>
  <el-config-provider :locale="locale">
    <router-view />
  </el-config-provider>
</template>

<script setup>
import locale from "element-plus/lib/locale/lang/zh-cn";
// import { userStore } from "store/modules/user";
// import { setRoutes } from "utils/user";
// import router from "@/router";

// if (user.token && router.getRoutes().length == 3) {
//   const user = userStore();
//   setRoutes(user.routes);
//   console.log("APP_-_-", user.routes);
// }
</script>

<style scoped></style>
