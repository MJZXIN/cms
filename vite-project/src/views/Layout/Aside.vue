<template>
    <el-radio-group v-model="isCollapse" style="margin-bottom: 0px">
        <el-radio-button :label="false" v-if="isCollapse">展开</el-radio-button>
        <el-radio-button :label="true" v-else="!isCollapse">折叠</el-radio-button>
    </el-radio-group>
    <el-scrollbar>
        <el-menu :default-active="router.currentRoute.value.fullPath" router collapse-transition class="el-menu-override" :collapse="isCollapse"
            @open="handleOpen" @close="handleClose">
            <template v-for="item of routes">
                <el-sub-menu :index="item.path" v-if="item.children.length > 0">
                    <template #title>
                        <el-icon>
                            <location />
                        </el-icon>
                        <span>{{ item.name }}</span>
                    </template>
                    <el-menu-item-group>
                        <!-- <template #title><span>{{ item.name }}</span></template> -->
                        <el-menu-item v-for="menu_item of item.children" :index="item.path + '/' + menu_item.path">{{
                            menu_item.name
                        }}</el-menu-item>
                    </el-menu-item-group>
                </el-sub-menu>
                <el-menu-item :index="item.path" v-else="item.children.length == 0">
                    <el-icon><icon-menu /></el-icon>
                    <template #title>{{ item.name }}</template>
                </el-menu-item>
            </template>
        </el-menu>
    </el-scrollbar>

</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { Menu as IconMenu } from '@element-plus/icons-vue'
import router from '@/router'
// 动态引入
// import {
//     Document,
//     Menu as IconMenu,
//     Location,
//     Setting,
// } from '@element-plus/icons-vue'

import { userStore } from '@/store';
const userInfo = userStore()
const rolelist = userInfo.userinfo.rolelist

const checkMenuRole = () => {
    let routeList = []
    routeList.push({
        path: '/',
        name: '首页',
        children: []
    })
    for (let route of userInfo.routes) {
        for (let role of rolelist) {
            if (route.roles.indexOf(role) < 0) {
                console.log("当前无权限使用此菜单")
            } else {
                route.children = checkSubMenuRole(route.children)
                routeList.push(route)
            }
        }
    }
    return routeList
}
const checkSubMenuRole = (children: any) => {
    let childrenList = []
    for (let route of children) {
        for (let role of rolelist) {
            if (route.roles.indexOf(role) < 0) {
                console.log("当前无权限使用此子菜单")
            } else {
                route.children = checkSubMenuRole(route.children)
                childrenList.push(route)
            }
        }
    }
    return childrenList
}
const routes = ref(checkMenuRole())
// const routes = ref(userInfo.routes)

const isCollapse = ref(false)
const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
</script>

<style>
.el-menu-override:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
}

.el-menu-override {
    height: calc(100vh - 100px);
}
</style>

<style scoped>
.el-scrollbar {
    height: calc(100vh - 100px);
}
</style>