import { createRouter, createWebHistory } from "vue-router";
import routes from "../router/routes";

const router = createRouter({
  routes,
  history: createWebHistory(),
});

const whiteList = ["/login", "/register", "/404"];
router.beforeEach((to, from, next) => {
  // user -> token
  if (whiteList.includes(to.path) || localStorage.getItem("USER_INFO")) {
    console.log("to: ", to.path);
    console.log("from ", from.path);
    if (
      (to.path == "/login" || to.path == "/register") &&
      localStorage.getItem("USER_INFO")
    ) {
      console.log("已登录, 请求被驳回, ", from.path);
      next("/" || from.path);
    }
    document.title = to.meta.title;
    next();
    // }
  } else {
    next("/login");
  }
});

export default router;
