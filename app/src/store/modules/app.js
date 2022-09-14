import { defineStore } from "pinia";

export const appStore = defineStore("APP_INFO", {
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
  getters: {
    getCollapse() {
      return state.menuCollapse;
    },
  },
  persist: {
    enabled: true,
    storage: sessionStorage,
  },
});
