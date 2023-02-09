<template>
    <div class="common-layout">
        <el-container>
            <!-- 将会影响 --el-header-height -->
            <el-header height="50px">Header</el-header>
            <el-container>
                <!-- 将会影响 --el-aside-width  -->
                <el-aside width="auto">
                    <Aside></Aside>
                </el-aside>
                <el-main>
                    <el-scrollbar>
                        <RouterView></RouterView>
                    </el-scrollbar>
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
.el-header {
    /* --el-header-height: 50px; */
    border-bottom: 1px solid #000;
}
.el-aside {
  /* width: auto; */
  height: calc(100vh - 50px);
}
</style>

<style scoped>
</style>