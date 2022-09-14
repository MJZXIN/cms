<template>
  <div class="title">CMS</div>
  <el-menu
    :default-active="this.$route.path"
    :collapse="app.menuCollapse"
    :collapse-transition="false"
    :route="true"
    :unique-opened="true"
    @select="handleSelect"
  >
    <template v-for="(i, index) in menuList">
      <el-menu-item v-if="i.children.length == 0" :index="i.path">
        <el-icon><component color="#111" :is="i.meta.icon" /></el-icon>
        <template #title>{{ i.meta.title }}</template>
      </el-menu-item>

      <el-sub-menu v-else :index="i.path || '/'">
        <template #title>
          <el-icon><component color="#111" :is="i.meta.icon" /></el-icon>
          <span>{{ i.name }}</span>
        </template>

        <el-menu-item-group v-for="j in i.children">
          <el-menu-item :index="i.path + j.path">
            <el-icon><component color="#111" :is="j.meta.icon" /></el-icon>
            <span>{{ j.meta.title }}</span></el-menu-item
          >
        </el-menu-item-group>
      </el-sub-menu>
    </template>
  </el-menu>
</template>

<script setup>
// import { Menu as IconMenu, Setting } from "@element-plus/icons-vue";
import router from "@/router";
import { userStore } from "@/store/modules/user";
import { appStore } from "store/modules/app";

const user = userStore();
const app = appStore();

let menuList = JSON.parse(user.$state.routes);

function filterMenu() {
  let newList = [];
  for (const i of menuList) {
    if (i.name != "404") {
      newList.push(i);
    }
    if (i.name == "home") {
      i.name = i.children[0].name;
      i.meta.title = i.children[0].meta.title;
      i.children = [];
    }
    if (i.name == "about") {
      i.name = i.children[0].name;
      i.meta.title = i.children[0].meta.title;
      i.children = [];
    }
    for (const j of i.children) {
      if (j.path.indexOf("/") != 0 && j.path != "") {
        j.path = "/" + j.path;
      }
    }
  }
  return newList;
}
menuList = filterMenu();
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
  router.push(key);
  // console.log(key, path, keyPath);
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
</style>
