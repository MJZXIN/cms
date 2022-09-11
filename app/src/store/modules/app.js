import { defineStore } from "pinia";

export const appStore = defineStore("app", {
  state: () => {
    return {
      menuCollapse: false,
    };
  },
  actions: {
    changeCollapse() {
      this.menuCollapse = !this.menuCollapse;
    },
  },
  getters: {},
});
