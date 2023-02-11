<template>
  <el-config-provider :locale="locale" :size="size" :z-index="zIndex">
    <router-view></router-view>
  </el-config-provider>
</template>

<script>
import { defineComponent, computed, ref } from 'vue'
import { ElConfigProvider } from 'element-plus'
import en from 'element-plus/dist/locale/en.mjs'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'

export default defineComponent({
  components: {
    ElConfigProvider,
  },
  setup() {
    const language = ref('zh_cn')
    const locale = computed(() => (language.value === 'zh_cn' ? zhCn : en))
    
    // language.value = language.value === 'zh-cn' ? 'en' : 'zh-cn'

    return {
      zIndex: 3000,
      size: 'default',
      locale: locale
    }
  },
})
</script>
