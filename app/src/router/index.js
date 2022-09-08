import { createRouter, createWebHistory } from "vue-router";
import routes from "../router/routes";
import NProgress from "nprogress";
import "nprogress/nprogress.css";
import { userStore } from "store/modules/user";

NProgress.configure({
  easing: "ease", // 动画方式
  speed: 500, // 递增进度条的速度
  showSpinner: false, // 是否显示加载ico
  trickleSpeed: 200, // 自动递增间隔
  minimum: 0.3, // 初始化时的最小百分比
});

const router = createRouter({
  routes,
  history: createWebHistory(),
});

const whiteList = ["/login", "/register", "/404"];
let registerRouteFresh = true;
const modules = import.meta.glob("../views/**/*.vue");

function getRoutes(item) {
  let routeList = [];
  for (const i in item) {
    let route = {
      ...item[i],
      component: modules[`${item[i].component}`],
      children: getRoutes(item[i].children),
    };
    routeList.push(route);
  }
  return routeList;
}

router.beforeEach((to, from, next) => {
  NProgress.start();
  const user = userStore();
  // if (whiteList.includes(to.path) || localStorage.getItem("USER_INFO")) {
  // console.log("to: ", to.path);
  // console.log("from ", from.path);
  // if (
  //   (to.path == "/login" || to.path == "/register") &&
  //   localStorage.getItem("USER_INFO")
  // ) {
  //   console.log("已登录, 请求被驳回, ", from.path);
  //   next("/" || from.path);
  // }
  if (registerRouteFresh && router.getRoutes().length < 4) {
    let item = [];
    try {
      item = JSON.parse(user.routes);
    } catch {}

    for (const i in item) {
      let route = {
        ...item[i],
        component: modules[`${item[i].component}`],
        children: getRoutes(item[i].children),
      };
      if (item[i].root) {
        router.addRoute(route);
      } else {
        router.addRoute(`${item[i].name}`, route);
      }
    }
    registerRouteFresh = false;
  } else {
    next();
  }

  if (whiteList.includes(to.path) || user.token) {
    // next();
    next({ ...to, replace: true });
  } else {
    next("/login");
  }
});

router.afterEach((to, from) => {
  // 在即将进入新的页面组件前，关闭掉进度条
  NProgress.done();
  document.title = to.meta.title;
});

export default router;
