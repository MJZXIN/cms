import { userStore } from "../store/modules/user";
import router from "@/router";
// import { USER_INFO_KEY, ROUTERS_KEY } from "@/store/cache-types";
import { filterAsyncRouter } from "utils/tool";

const store = userStore();

const modules = import.meta.glob("../views/**/*.vue");

export async function setUserInfo(info) {
  //   localStorage.setItem(USER_INFO_KEY, JSON.stringify(info));

  // const deepCopy = JSON.parse(JSON.stringify(info.routes));
  const deepCopy = info.routes;
  const accessedRouters = filterAsyncRouter(deepCopy, info.userinfo.userrole);
  //   localStorage.setItem(ROUTERS_KEY, JSON.stringify(accessedRouters));
  store.$patch((state) => {
    state.token = "Bearer " + info.token;
    state.userInfo = JSON.stringify(info.userinfo);
    state.routes = JSON.stringify(accessedRouters);
  });

  const newRoutes = getRoutes(accessedRouters);
  for (const i of newRoutes) {
    router.addRoute(i);
  }
}

// 返回路由的基本格式
export function getRoutes(item) {
  let routes = [];
  for (const i in item) {
    let route = {
      ...item[i],
      component: modules[`${item[i].component}`],
      children: getRoutes(item[i].children),
    };
    routes.push(route);
  }
  return routes;
}

/**
 * 设置动态路由
 **/
export function setRoutes(routes) {
  // const routes = store.routes;
  for (const i of routes) {
    router.addRoute(i);
  }
}
