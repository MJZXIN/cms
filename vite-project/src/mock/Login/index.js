const login = {
    url: "/api/mock/login",
    method: "post",
    response: () => {
      return {
        "code": 200,
        "data": {
          "routes": [
            {
              "children": [
                {
                  "children": [],
                  "component": "../views/System/user.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Memo",
                    "title": "用户管理"
                  },
                  "name": "用户设置",
                  "path": "user",
                  "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/System/role.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Memo",
                    "title": "角色管理"
                  },
                  "name": "角色设置",
                  "path": "role",
                  "roles": [
                    "ADMIN",
                    "SYSTEM"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/System/post.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Menu",
                    "title": "岗位管理"
                  },
                  "name": "岗位管理",
                  "path": "post",
                  "roles": [
                    "ADMIN",
                    "SYSTEM"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/System/dept.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Menu",
                    "title": "部门管理"
                  },
                  "name": "部门管理",
                  "path": "dept",
                  "roles": [
                    "ADMIN",
                    "SYSTEM"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/System/corp.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Menu",
                    "title": "公司管理"
                  },
                  "name": "公司管理",
                  "path": "corp",
                  "roles": [
                    "SYSTEM"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/System/menu.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Menu",
                    "title": "菜单管理"
                  },
                  "name": "菜单管理",
                  "path": "menu",
                  "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/System/dict.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Menu",
                    "title": "字典管理"
                  },
                  "name": "字典管理",
                  "path": "dict",
                  "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/System/config.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Menu",
                    "title": "参数设置"
                  },
                  "name": "参数设置",
                  "path": "config",
                  "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/Setting/system.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Memo",
                    "title": "系统设置"
                  },
                  "name": "系统设置",
                  "path": "setting",
                  "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                  ]
                }
              ],
              "component": "../views/Layout/index.vue",
              "hidemenu": "False",
              "meta": {
                "icon": "Setting",
                "title": "系统管理"
              },
              "name": "系统管理",
              "path": "/system",
              "roles": [
                "ADMIN",
                "SYSTEM",
                "USER"
              ]
            },
            {
              "children": [
                {
                  "children": [],
                  "component": "../views/Product/product.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "SetUp",
                    "title": "物料管理"
                  },
                  "name": "产品管理",
                  "path": "",
                  "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/Product/part.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "SetUp",
                    "title": "零件管理"
                  },
                  "name": "零件管理",
                  "path": "part",
                  "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/Product/cost.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Notebook",
                    "title": "成本管理"
                  },
                  "name": "成本管理",
                  "path": "cost",
                  "roles": [
                    "ADMIN",
                    "SYSTEM"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/Product/bom.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Guide",
                    "title": "BOM管理"
                  },
                  "name": "BOM管理",
                  "path": "bom",
                  "roles": [
                    "ADMIN",
                    "SYSTEM"
                  ]
                },
                {
                  "children": [],
                  "component": "../views/Master/warehouse.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Guide",
                    "title": "仓库管理"
                  },
                  "name": "仓库管理",
                  "path": "warehouse",
                  "roles": [
                    "ADMIN",
                    "SYSTEM"
                  ]
                }
              ],
              "component": "../views/Layout/layout.vue",
              "hidemenu": "False",
              "meta": {
                "icon": "SetUp",
                "title": "主数据管理"
              },
              "name": "主数据管理",
              "path": "/master",
              "roles": [
                "ADMIN",
                "SYSTEM",
                "USER"
              ]
            },
            {
              "children": [
                {
                  "children": [],
                  "component": "../views/About/index.vue",
                  "hidemenu": "False",
                  "meta": {
                    "icon": "Help",
                    "title": "关于"
                  },
                  "name": "关于",
                  "path": "",
                  "roles": [
                    "ADMIN",
                    "SYSTEM",
                    "USER"
                  ]
                }
              ],
              "component": "../views/Layout/index.vue",
              "hidemenu": "False",
              "meta": {
                "icon": "Help",
                "title": "关于"
              },
              "name": "about",
              "path": "/about",
              "roles": [
                "ADMIN",
                "SYSTEM",
                "USER"
              ]
            }
          ],
          "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6Imp3dCJ9.eyJ1c2VybmFtZSI6IlNZU1RFTSIsInJvbGVuYW1lIjoiVVNFUiIsImV4cCI6MTY3NjQ0ODc0Nn0.t94pf_nEnCeVtBu-05pnDUiS21mWr43UaaFeZlNAI3k",
          "userinfo": {
            "rolelist": [
              "USER"
            ],
            "username": "SYSTEM"
          }
        },
        "msg": "登录成功"
      }
    }
}
export {
    login
}