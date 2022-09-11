<template>
  <div class="common-layout">
    <el-container>
      <el-aside :width="isCollapse ? '64px' : '200px'"
        ><Aside></Aside
      ></el-aside>
      <el-container>
        <el-header><Header></Header></el-header>
        <el-breadcrumb separator=">">
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <!-- <el-breadcrumb-item><a href="/">首页</a></el-breadcrumb-item> -->
          <el-breadcrumb-item>首页</el-breadcrumb-item>
        </el-breadcrumb>
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Aside from "components/Layout/Aside.vue";
import Header from "components/Layout/Header.vue";
import { appStore } from "@/store/modules/app";
import { ref } from "vue";

let menuWidth = ref(localStorage.getItem("Collapse") || "200px");

export default {
  name: "layout",
  data() {
    return {
      isCollapse: false,
    };
  },
  components: {
    Aside,
    Header,
  },
  created() {
    const app = appStore();
    // if (app.menuCollapse) {
    //   menuWidth = "200px";
    // } else {
    //   menuWidth = "64px";
    // }
    this.isCollapse = app.menuCollapse;
    localStorage.setItem("Collapse", menuWidth);
  },
  computed: {
    stylelVar() {
      return {
        "--collapse-width": "64px",
      };
    },
  },
};
</script>

<style>
.el-header {
  height: 50px;
  padding: 0;
}

.el-aside {
  min-height: 100vh;
}
</style>
