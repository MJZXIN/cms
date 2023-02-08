<template>
    <div class="common-layout">
        <el-container>
            <el-header style="height: 50px;">Header</el-header>
            <el-container>
                <el-aside width="auto">
                    <Aside></Aside>
                </el-aside>
                <el-main>
                    <RouterView></RouterView>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
import Aside from './Aside.vue'
export default {
    components: {
        Aside
    }
}
</script>

<style>
/* TODO： 尝试修改--el-aside-width的值 */
.el-aside {
  /* width: auto; */
  height: calc(100vh - 50px);
}
</style>