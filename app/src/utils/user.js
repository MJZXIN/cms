import { userStore } from "../store/modules/user";
import routes from "@/router/routes";
// import { USER_INFO_KEY, ROUTERS_KEY } from "@/store/cache-types";
import { filterAsyncRouter } from "utils/tool";

const store = userStore();

export async function setUserInfo(info) {
  //   localStorage.setItem(USER_INFO_KEY, JSON.stringify(info));

  const deepCopy = JSON.parse(JSON.stringify(routes));
  const accessedRouters = filterAsyncRouter(deepCopy, info.role);

  //   localStorage.setItem(ROUTERS_KEY, JSON.stringify(accessedRouters));
  store.$patch((state) => {
    state.token = "Bearer " + info.token;
    state.userInfo = JSON.stringify(info.userinfo);
    state.routes = JSON.stringify(accessedRouters);
  });
}

// export async function getToken() {
//   return state.$state.token || JSON.parse(localStorage.getItem("USER_INFO"));
// }

// export async function getUserInfo() {
//   return state.$state.userInfo || JSON.parse(localStorage.getItem("USER_INFO"));
// }

// export async function getRouters() {
//   return state.$state.routers.length > 0
//     ? state.$state.routers
//     : JSON.parse(localStorage.getItem(ROUTERS_KEY));
// }
