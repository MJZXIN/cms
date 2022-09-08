<template>
  <div class="title">CMS</div>
  <el-menu
    :default-active="router.currentRoute.value.path"
    class="el-menu-vertical-demo"
    :collapse="false"
    :collapse-transition="true"
    :route="true"
    :unique-opened="true"
    @select="handleSelect"
  >
    <template v-for="(i, index) in menuList">
      <el-menu-item v-if="i.children.length == 0" :index="i.path || '/'">
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
            <span>{{ j.meta.title }}</span></el-menu-item
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
import { userStore } from "@/store/modules/user";

const user = userStore();

let menuList = JSON.parse(user.$state.routes);

function filterMenu() {
  let newList = [];
  for (const i of menuList) {
    if (i.name != "404") {
      newList.push(i);
    }
    if (i.name == "home") {
      i.path = i.children[0].path;
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
