import { MockMethod } from 'vite-plugin-mock'

export default [
  {
    url: "/api/mock/login",
    method: "post",
    response: () => {
      return {
        code: 200,
        message: "ok",
        data: {
          "token": "abcdefg",
          "routes": [{
            path: "/view",
            component: "../views/View/index.vue",
            children: [],
            meta: {
              title: '看板',
              hideMenu: false, //加入hideMenu属性，不展示在侧边栏
            },
            name: "view",
          },
          {
            path: "/setting",
            component: "../views/Setting/index.vue",
            children: [],
            meta: {
              title: "设置",
              hideMenu: false,
            },
            name: 'setting',
            // hideMenu: true,//不展示在侧边栏
          }
          ]
        }
      };
    }
  }
] as MockMethod[]