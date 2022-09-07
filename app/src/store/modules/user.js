import { defineStore } from "pinia";

export const userStore = defineStore("USER_INFO", {
  state: () => {
    return {
      token: "",
      userInfo: null,
      routes: [],
    };
  },
  persist: {
    enabled: true,
    // key: ["token"],
    encryptionKey: "xxPqNwkq32Hfm6A9ZM8WFSCZLBX8",
    storage: localStorage,
  },
});
