<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">Aside</el-aside>
      <el-container>
        <el-header>Header</el-header>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
// import 'element-plus/theme-chalk/index.css'
export default {
  name: "layout",
  // data() {
  //   return {

  //   }
  // }
}
</script>

<style>
</style>