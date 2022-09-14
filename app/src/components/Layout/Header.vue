<template>
  <div class="header-line">
    <div style="height: 50px; display: flex; float: left">
      <el-icon :size="28" class="collapseBut" @click="changeCollapse">
        <component color="#111" :is="menuState" />
      </el-icon>
    </div>
    <div style="line-height: 50px; flex: 1; padding: 18px 10px; float: left">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item><a href="/">**管理</a></el-breadcrumb-item>
        <el-breadcrumb-item>{{ this.$route.meta.title }}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div style="height: 40px; float: right">
      <el-dropdown style="padding: 5px 20px">
        <el-avatar :icon="Expand" />
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item>Action 1</el-dropdown-item>
            <el-dropdown-item>Action 2</el-dropdown-item>
            <el-dropdown-item>Action 3</el-dropdown-item>
            <el-dropdown-item>Action 4</el-dropdown-item>
            <el-dropdown-item @click="user_logout">退出</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
      <div style="line-height: 50px; padding: 0 10px 0 0; float: right">
        {{ cur_user }}
      </div>
    </div>
  </div>
</template>

<script>
import { Fold, Expand, UserFilled } from "@element-plus/icons-vue";
import { ref } from "vue";
import { appStore } from "store/modules/app";
import { userStore } from "@/store/modules/user";
import { logout } from "api";
import router from "router";

export default {
  name: "Header",
  data() {
    return {
      menuState: "Fold",
      cur_user: "",
    };
  },
  components: {
    UserFilled,
  },
  methods: {
    changeCollapse() {
      const app = appStore();
      app.changeCollapse();
      this.menuState = app.menuCollapse ? "Expand" : "Fold";
    },
    user_logout() {
      logout();
      localStorage.clear();
      router.replace("/login");
    },
  },
  created() {
    const app = appStore();
    this.menuState = app.menuCollapse ? "Expand" : "Fold";
    const user = userStore();
    this.cur_user = JSON.parse(user.userInfo).username;
  },
};
</script>

<style scoped>
.title {
  display: inline-block;
  text-align: center;
  line-height: 50px;
  width: 100%;
  /* background-color: rgb(236, 245, 255); */
}

.collapseBut {
  cursor: pointer;
  margin: 11px;
}

.header-line {
  display: flex;
  justify-content: space-between;
  /* line-height: 50px; */
  margin: auto;
}
</style>
