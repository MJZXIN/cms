const actions = {
  generateRoutes({ commit }) {
    return new Promise((resolve) => {
      menu({ username: storage.getItem("username") }).then((response) => {
        let accessedRoutes = filterAsyncRoutes(response.data);
        commit("SET_ROUTES", accessedRoutes);
        resolve(accessedRoutes);
      });
    });
  },
};

export function filterAsyncRoutes(routes) {
  const async = routes.filter((route) => {
    if (route.component) {
      route.component = Layout;
      if (route.children && route.children.length) {
        route.children.forEach((item) => {
          item.component = loadView(item.component);
        });
        return true;
      }
      return true;
    }
    return true;
  });
  return async;
}

/**
 * 路由懒加载 拼接
 * @param view
 * @returns {function(): *}
 */
export const loadView = (view) => {
  // 这里需要注意一下 vite+vue3 要用 defineAsyncComponent 才能拼接成功 不然会一直报错找不到模块  加上/* @vite-ignore */ 可以不显示警告
  return () =>
    defineAsyncComponent(() => import(/* @vite-ignore */ `/src/${view}.vue`));
};

const mutations = {
  SET_ROUTES: (state, routes) => {
    state.addRoutes = routes;
    // 过滤掉不需要显示在菜单栏的公共菜单 并格式化
    let constant = filterConstantRoutes(constantRoutes);
    state.routes = constant.concat(routes);
  },
};

/**
 * 过滤递归公共路由
 * @param routes
 * @returns {*[]}
 */
export function filterConstantRoutes(routes) {
  const router = routes.filter((item) => !item.hidden);
  const routeList = [];
  for (const item of router) {
    let temp = {};
    if (!item.alwaysShow && item.children.length) {
      temp.path = item.path;
      temp.meta = item.children[0].meta;
      temp.alwaysShow = false;
      routeList.push(temp);
    } else {
      routeList.push(item);
    }
  }
  return routeList;
}
