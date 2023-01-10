router.beforeEach(async (to, from, next) => {
  var requestUrl = "http://127.0.0.1:8000/api/system/menus/";
  await axios
    .get(requestUrl)
    .then(res => {
      for (var i = 0; i < res.data.length; i++) {
        var te = {
          path: res.data[i].url,
          name: res.data[i].name,
          component: () => import('@/views/Sys/Jingchuan.vue')
        };
      }
      
    .catch ((res) => {
        console.log("except");
      });


  if (to.path === '/login') {
    // 如果是访问登录界面，如果用户会话信息存在，代表已登录过，跳转到主页
    if (token) {
      next({ path: '/' })
    } else {
      next()
    }
  } else {
    if (!token) {
      // 如果访问非登录界面，且户会话信息不存在，代表未登录，则跳转到登录界面
      next({ path: '/login' })
    } else {
      // 加载动态菜单和路由
      for (var i = 0; i < dd.length; i++) {
        router.addRoute('Home', dd[i]);
        router.options.routes.push(dd[i]);
        //router.push(dd[i].path)
        console.log(router);
      }
      console.log(router.getRoutes());
      store.commit('menuRouteLoaded', true)

      next()
    }

  }

})