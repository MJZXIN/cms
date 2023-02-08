import { createRouter, createWebHistory } from "vue-router";
import NProgress from "nprogress";
import "nprogress/nprogress.css";
import { userStore } from "../store";
import addRoutes from './addRouter'

const routes = [
    {
        path: "/login",
        name: "Login",
        component: () => import("../views/Login/index.vue"),
        meta: {
            title: '登录页',
            hideMenu: true, //加入hideMenu属性，不展示在侧边栏
        },
        children: []
    },
    {
        path: "/",
        name: 'HomePage',
        component: () => import("../views/Layout/index.vue"),
        meta: {
            keepalive: true,
            title: "主页",
        },
        // hideMenu: true,//不展示在侧边栏
        redirect: '',
        children: [{
            path: "",
            name: 'Home',
            component: () => import("../views/Layout/home.vue"),
            meta: {
                keepalive: true,
                title: "主页",
            },
            // hideMenu: true,//不展示在侧边栏
            redirect: '',
            children: []
        }]
    },
    // {
    //     path: "/:pathMatch(.*)",
    //     name: "4041",
    //     component: () => import("../views/Error/404.vue"),
    //     children: [],
    //     meta: {
    //         title: '404',
    //         hideMenu: true, //加入hideMenu属性，不展示在侧边栏
    //     }
    // },
    {
        path: "/404",
        name: "404",
        component: () => import("../views/Error/404.vue"),
        meta: {
            title: '迷路了',
            hideMenu: true, //加入hideMenu属性，不展示在侧边栏
        },
        children: [],
    }]

const router = createRouter({
    history: createWebHistory('/'),
    routes, // `routes: routes` 的缩写
})

// console.log(this)


//TODO 要删除

// console.log("./router/index: User Token", userInfo.$state.token)

router.beforeEach(async (to, from, next) => {
    NProgress.start()
    const userInfo = userStore()
    if (userInfo.token) {
        if (to.path == '/login') {
            // next('/')
            next()
        } else {
            // 能够访问的情况
            // if (router.getRoutes().length > routes.length) {
            if (router.getRoutes().length > routes.length + 1) {
                console.log("路由大于2个")
                // 不在路由中的地址会显示undefined, 通过这个可以判断404
                if (to.meta.title == undefined) {
                    console.log("***404 because this URL: ", to.path)
                    next('/404')
                } else {
                    next()
                }
            } else {
                await addRoutes(router);
                console.log(router.getRoutes().length)
                // next()   
                next({
                    ...to,
                    replace: true
                })
            }
        }
    } else {
        if (to.path == '/login') {
            next()
        }
        next('/login')
    }

    // if (userInfo.token) {
    //     if (to.path == '/login') {
    //         next({
    //             path: '/'
    //         })
    //     } else {
    //         // TODO 要删除true
    //         if (userInfo.getters['login/getRoutes'].length || to.name != null || true) {
    //             next()
    //         } else {
    //             await addRoutes();
    //             next({
    //                 ...to,
    //                 replace: true
    //             })
    //         }
    //     }
    // } else {
    //     if (to.path == '/login') {
    //         next()
    //     } else {
    //         next('/login')
    //     }
    // }
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

export default router;