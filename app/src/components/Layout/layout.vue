<template>
  <div class="common-layout">
    <el-container>
      <el-aside><Aside></Aside></el-aside>
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
export default {
  name: "layout",
  components: {
    Aside,
    Header,
  },
};
</script>

<style scoped>
.el-header {
  height: 50px;
  padding: 0;
}

.el-aside {
  width: 200px;
  min-height: 100vh;
}
</style>
