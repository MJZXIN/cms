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
    document.title = to.meta.title;
    next();
  } else {
    next("/login");
    // next("/");
  }
});

export default router;
