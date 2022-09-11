<template>
  <span style="display: inline-block"
    ><button @click="changeCollapse" style="display: inline-block">切换</button>
    <span class="title">Header</span></span
  >
</template>

<script>
import { appStore } from "store/modules/app";
import { ref } from "vue";
let menuState = ref("false");

export default {
  name: "Header",
  methods: {
    changeCollapse() {
      const app = appStore();
      app.changeCollapse();
      menuState = app.menuCollapse;
    },
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
</style>
