import { createRouter, createWebHistory } from "vue-router";
import routes from "../router/routes";
import NProgress from "nprogress";
import "nprogress/nprogress.css";
import { userStore } from "store/modules/user";

NProgress.configure({
  easing: "ease", // 动画方式
  speed: 500, // 递增进度条的速度
  showSpinner: true, // 是否显示加载ico
  trickleSpeed: 200, // 自动递增间隔
  minimum: 0.3, // 初始化时的最小百分比
});

const router = createRouter({
  routes,
  history: createWebHistory(),
});

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
const whiteList = ["/login", "/register", "/404"];
let registerRouteFresh = true;

router.beforeEach((to, from, next) => {
  NProgress.start();
  const user = userStore();

  // 判断是否是白名单
  if (whiteList.includes(to.path)) {
    console.log("白名单");
    next();
  } else {
    if (user.token) {
      console.log("检测到有Token信息");
      //添加路由
      if (router.getRoutes().length < 4 || registerRouteFresh) {
        console.log(user.token);
        console.log("首次进入");
        let item = [];
        try {
          item = JSON.parse(user.routes);
        } catch {
          console.log("路由信息错误!!!");
        }
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
        next({ ...to, replace: true });
      } else {
        console.log("再次进入");
        next();
      }
    } else {
      next("/login");
    }
  }
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

  // if (whiteList.includes(to.path) || user.token) {
  //   // next();
  //   // next({ ...to, replace: true });
  // } else {
  //   next("/login");
  // }
  // // 刷新前
  // if (router.getRoutes().length < 4) {
  //   console.log("首次进入");
  //   let item = [];
  //   try {
  //     item = JSON.parse(user.routes);
  //   } catch {}
  //   for (const i in item) {
  //     let route = {
  //       ...item[i],
  //       component: modules[`${item[i].component}`],
  //       children: getRoutes(item[i].children),
  //     };
  //     if (item[i].root) {
  //       router.addRoute(route);
  //     } else {
  //       router.addRoute(`${item[i].name}`, route);
  //     }
  //   }
  //   registerRouteFresh = false;
  //   next({ ...to, replace: true });
  // } else {
  //   console.log("再次进入");
  //   console.log(router.getRoutes());
  //   next();
  // }
});

router.afterEach((to, from) => {
  // 在即将进入新的页面组件前，关闭掉进度条
  NProgress.done();
  document.title = to.meta.title;
});

export default router;
