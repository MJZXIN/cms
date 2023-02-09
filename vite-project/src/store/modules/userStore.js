import { defineStore } from "pinia"

export const userStore = defineStore('USER', {
    // 其他配置...
    state: () => {
        return {
            token: null,
            routes: [],
            userinfo: {
                username: '',
                rolelist: []
            }
        }
    },
    actions: {
        setToken(token) {
            this.token = token
        },
        setRoutes(routes) {
            this.routes = routes
        },
        setUserInfo(userinfo) {
            this.userinfo = userinfo
        }
    },
    persist: {
        enabled: true,
        // key: ["token"],
        // encryptionKey: "xxPqNwkq32Hfm6A9ZM8WFSCZLBX8",
        storage: localStorage,
    },
})