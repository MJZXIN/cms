import { defineStore } from "pinia"

export const userStore = defineStore('USER', {
    // 其他配置...
    state: () => {
        return {
            token: null,
            routes: []
        }
    }, persist: {
        enabled: false,
        // key: ["token"],
        // encryptionKey: "xxPqNwkq32Hfm6A9ZM8WFSCZLBX8",
        storage: localStorage,
    },
})