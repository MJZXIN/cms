let asyncRoutes = [] //定义数组接收后端返回的路由

const routeAllPathToCompMap = import.meta.glob(`../view/**/*.vue`);
//**为通配符,vite不支持require导入方式,故用import.meta.glob(vite动态导入)
/*import.meta.glob
 * 该方法匹配到的文件默认是懒加载，通过动态导入实现，构建时会分离独立的 chunk，是异步导入，返回的是 Promise
 * /*import.meta.globEager
 * 该方法是直接导入所有模块，并且是同步导入，返回结果直接通过 for...in循环就可以操作
 */
async function addRoutes() {
    await store.dispatch('login/getNewRoutes').then((res) => { //获取后端返回的动态路由
        if (res.data && res.data.length) {
            // let homeRouteChildren = [];
            asyncRoutes = res.data;
            /*
             * 1。拿到处理完毕home的children，最终替换掉原来的children，给菜单渲染提供支持
             * 2.通过递归,调用router.addRoute,把每一项route插到对应的父route下
             */
            //服务端配置了路由，但前端还没添加对应文件的路由列表，内容是路由的component值(服务端的)
            // const unForList = ['']
            const homeChildren = routes[1].children;
            const dfs = (parentRouteName = 'Home', asyncRoutes = [], originRouteChildren = []) => {
                if (!Array.isArray(asyncRoutes)) return [];
                asyncRoutes.forEach(route => {
                    // if (unForList.includes(route.component)) return;
                    /**后端返回来的路由component是字符串,如component: "view/Index/index.vue",
                     * 前端需要把component: "view/Index/index.vue" 转化为组件对象
                     * component:() => import("/src/view/Index/index.vue")
                    **/
                    route.component = routeAllPathToCompMap[`../${route.component}`];
                    // route.component = () => import(`../${route.component}`);
                    const routeChildren = route.children;

                    router.addRoute(parentRouteName, route);

                    route.children = dfs(route.name, routeChildren)

                    originRouteChildren.push(route)
                })
                return originRouteChildren
            }
            // homeRouteChildren = dfs(asyncRoutes)
            dfs('Home', asyncRoutes, homeChildren)
        }
    });
}