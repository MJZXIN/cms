<template>
  <div>
    <el-container>
      <el-aside :style="{ width: menuWidth }">
        <Aside></Aside>
      </el-aside>
      <el-container>
        <el-header><Header></Header></el-header>
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
import Bread from "components/Layout/Bread.vue";
import { appStore } from "@/store/modules/app";
import { ref } from "vue";

export default {
  name: "layout",
  data() {
    return {
      menuWidth: "200px",
    };
  },
  components: {
    Aside,
    Header,
    Bread,
  },
  created() {
    // const app = appStore();
    // this.menuWidth = app.menuCollapse ? "64px" : "200px";
    // console.log(this.menuWidth);
    const app = appStore();
    // let menuWidth = ref("200px");
    this.menuWidth = app.menuCollapse ? "auto" : "200px";
    const subscribe = app.$subscribe(
      (mutation, state) => {
        this.menuWidth = app.menuCollapse ? "auto" : "200px";
      },
      {
        detached: false,
      }
    );
  },
  setup() {
    // const app = appStore();
    // let menuWidth = ref("200px");
    // let isCollapse = false;
    // const subscribe = app.$subscribe(
    //   (mutation, state) => {
    //     this.menuWidth = app.menuCollapse ? "64px" : "200px";
    //     isCollapse = app.menuCollapse;
    //     console.log(isCollapse, menuWidth);
    //   },
    //   {
    //     detached: false,
    //   }
    // );
    // return { isCollapse };
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
