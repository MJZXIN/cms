import layout from "@/views/layout/layout.vue";
const modules = import.meta.glob("../views/**/*.vue");

const routes = [
  // {
  //   path: "/",
  //   component: layout,
  //   meta: {
  //     title: "首页",
  //   },
  //   children: [
  //     {
  //       path: "/",
  //       name: "dashboard",
  //       component: () => import("views/home/dashboard.vue"),
  //     },
  //   ],
  // },
  {
    path: "/login",
    component: modules["../views/auth/login.vue"],
    meta: {
      title: "登录",
    },
    children: [],
  },
  {
    path: "/register",
    component: () => import("views/auth/register.vue"),
    meta: {
      title: "注册",
    },
    children: [],
  },
  {
    path: "/404",
    component: () => import("views/error/404.vue"),
    meta: {
      title: "404",
    },
    children: [],
  },
];

export default routes;
