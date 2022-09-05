import { defineStore } from "pinia";

export const userStore = defineStore("user", {
  state: () => {
    return {
      count: 1,
    };
  },
  actions: {
    countAdd() {
      this.count++;
    },
  },
  getters: {
    countSum(state) {
      return state.count * 2;
    },
  },
});
