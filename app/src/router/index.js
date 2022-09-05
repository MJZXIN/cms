import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("../components/layout.vue"),
    children: [
      {
        path: "/",
        name: "dashboard",
        component: () => import("views/home/dashboard.vue"),
      },
    ],
  },
  {
    path: "/login",
    component: () => import("views/auth/login.vue"),
    meta: {
      title: "登录",
    },
  },
  {
    path: "/register",
    component: () => import("views/auth/register.vue"),
    meta: {
      title: "注册",
    },
  },
  {
    path: "/404",
    component: () => import("views/error/404.vue"),
    meta: {
      title: "404",
    },
  },
  {
    path: "/*",
    component: () => import("views/error/404.vue"),
    meta: {
      title: "404",
    },
  },
];
const router = createRouter({
  routes,
  history: createWebHistory(),
});

const whiteList = ["/login", "/register", "/404"];
router.beforeEach((to, from, next) => {
  if (whiteList.includes(to.path) || localStorage.getItem("token")) {
    document.title = to.meta.title;
    next();
  } else {
    // next("/login");
    next("/");
  }
});

export default router;
