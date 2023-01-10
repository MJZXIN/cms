<template>
    <el-config-provider :size="size" :z-index="zIndex">
      <app />
    </el-config-provider>
  </template>
  
  <script>
  import { defineComponent } from 'vue'
  import { ElConfigProvider } from 'element-plus'
  
  export default defineComponent({
    components: {
      ElConfigProvider,
    },
    setup() {
      return {
        zIndex: 3000,
        size: 'small',
      }
    },
  })
  </script>