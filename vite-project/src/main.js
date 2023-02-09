import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { store } from './store'
import router from "./router"
import * as ElementPlusIconsVue from '@element-plus/icons-vue'


// TODO: 实现国际化
// import lang_en from 'element-plus/lib/locale/lang/en'
// import locale from 'element-plus/lib/local'

const app = createApp(App)
app.use(store)
app.use(router)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
/* 自定义指令 utils/directive/permission/index
import * as directive from "@/directive";

Object.keys(directive).forEach(key => {
    app.directive(key, (directive as { [key: string]: Directive })[key]);
});
*/

app.mount('#app')
