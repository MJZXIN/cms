import { createI18n } from 'vue-i18n'
/*
 * The i18n resources in the path specified in the plugin `include` option can be read
 * as vue-i18n optimized locale messages using the import syntax
 */
import zh_cn from '@/locales/zh_cn.json'
import en from '@/locales/en.json'

const i18n = createI18n({
  locale: 'zh_cn',
  messages: {
    zh_cn,
    en
  }
})

export default i18n