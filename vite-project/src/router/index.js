import userStore from "../store";
import { createRouter, createWebHistory } from "vue-router";
import NProgress from "nprogress";
import "nprogress/nprogress.css";

const routes = [{
    path: "/login",
    component: () => import("../views/Login/index.vue"),
    children: [],
    meta: {
        title: '登录页',
        hideMenu: true, //加入hideMenu属性，不展示在侧边栏
    },
    name: "Login",
},
{
    path: "/",
    component: () => import("../views/Home/index.vue"),
    children: [],
    meta: {
        keepalive: true,
        title: "主页",
    },
    name: 'Home',
    // hideMenu: true,//不展示在侧边栏
    redirect: ''
}
]

const router = createRouter({
    history: createWebHistory('/'),
    routes, // `routes: routes` 的缩写
})

const userInfo = userStore.state

//TODO 要删除
console.log("./router/index: User Token", userInfo.token)

router.beforeEach(async (to, from, next) => {
    if (userInfo.token) {
        if (to.path == '/login') {
            next({
                path: '/'
            })
        } else {
            // TODO 要删除true
            if (userInfo.getters['login/getRoutes'].length || to.name != null || true) {
                next()
            } else {
                await addRoutes();
                next({
                    ...to,
                    replace: true
                })
            }
        }
    } else {
        if (to.path == '/login') {
            next()
        } else {
            next('/login')
        }
    }
})

NProgress.configure({
    easing: "ease", // 动画方式
    speed: 500, // 递增进度条的速度
    showSpinner: true, // 是否显示加载ico
    trickleSpeed: 200, // 自动递增间隔
    minimum: 0.3, // 初始化时的最小百分比
});

router.afterEach((to, from) => {
    // 在即将进入新的页面组件前，关闭掉进度条
    NProgress.done();
    document.title = to.meta.title;
});

const modules = import.meta.glob("../views/**/*.vue");
for (let item in modules) {
    console.log(item.split('/'))
    let str = item.split('/')
    if (!(item.search('login') || item.search('home'))) {
        router.addRoute({
            path: "/" + str[2],
            component: modules[item],
            children: [],
            meta: {
                title: str[2],
                hideMenu: true, //加入hideMenu属性，不展示在侧边栏
            },
            name: str[2],
        })
    }
}
console.log(router.getRoutes())

export default router;