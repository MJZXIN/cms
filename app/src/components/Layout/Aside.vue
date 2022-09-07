<template>
  <div class="title">CMS</div>
  <el-menu
    :default-active="this.$route.path"
    class="el-menu-vertical-demo"
    :collapse="false"
    collapse-transition="true"
    route="true"
    @select="handleSelect"
  >
    <template v-for="(i, index) in routes">
      <el-menu-item v-if="i.children.length == 0" :index="i.path">
        <el-icon><icon-menu /></el-icon>
        <template #title>{{ i.meta.title }}</template>
      </el-menu-item>

      <el-sub-menu v-if="i.children.length > 0" :index="i.path">
        <template #title>
          <el-icon><Setting /></el-icon>
          <span>{{ i.meta.title }}</span>
        </template>
        <el-menu-item-group v-for="j in i.children">
          <!-- <template #title><span>Group One</span></template> -->
          <el-menu-item :index="j.path"
            ><el-icon><Setting /></el-icon>
            <span>{{ j.name }}</span></el-menu-item
          >
        </el-menu-item-group>
        <!-- <el-sub-menu index="1-4">
          <template #title><span>item four</span></template>
          <el-menu-item index="1-4-1">item one</el-menu-item>
        </el-sub-menu> -->
      </el-sub-menu>
    </template>
  </el-menu>
</template>

<script setup>
import { Menu as IconMenu, Setting } from "@element-plus/icons-vue";
import router from "@/router";
import { computeStyles } from "@popperjs/core";

const routes = [
  {
    path: "/",
    component: "components/Layout/layout.vue",
    meta: {
      title: "首页",
    },
    children: [],
  },
  {
    path: "/setting",
    component: "components/Layout/layout.vue",
    meta: {
      title: "设置",
    },
    children: [
      {
        path: "/system",
        name: "系统设置",
        component: "views/home/dashboard.vue",
      },
      {
        path: "/user",
        name: "用户设置",
        component: "views/home/dashboard.vue",
      },
    ],
  },
];

// const handleOpen = (key, keyPath) => {
//   console.log(key, keyPath);
// };
// const handleClose = (key, keyPath) => {
//   console.log(key, keyPath);
// };
const handleSelect = (key, keyPath) => {
  let path = "";
  for (const i in keyPath) {
    path = path + keyPath[i];
  }
  router.push(path);
};
</script>

<style scoped>
.title {
  display: inline-block;
  text-align: center;
  line-height: 50px;
  width: 100%;
  background-color: rgb(64, 158, 255);
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
</style>
