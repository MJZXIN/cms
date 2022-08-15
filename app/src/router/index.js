import { createRouter, createWebHistory } from "vue-router"

const routes = [
    {
        path: "/",
        component: () => import('../components/layout.vue'),
        children: [
            {
                path: '/',
                name: 'dashboard',
                component: () => import('views/home/dashboard.vue')
            }
        ]
    }, {
        path: "/login",
        component: () => import('views/login.vue'),
        meta: {
            title: "登录"
        }
    }, {
        path: "/registry",
        component: () => import('views/registry.vue'),
        meta: {
            title: "注册"
        }
    }, {
        path: "/404",
        component: () => import('views/errorpages/404.vue'),
        meta: {
            title: "404"
        }
    }
]
const router = createRouter({
    routes,
    history: createWebHistory()
})

const whiteList = ['/login', '/registry', '/404']
router.beforeEach((to, from, next) => {
    if (whiteList.includes(to.path) || localStorage.getItem("token")) {
        document.title = to.meta.title
        next()
    } else {
        next("/login")
    }
})

export default router