import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { store } from './store'
import router from "./router"


// TODO: 实现国际化
// import lang_en from 'element-plus/lib/locale/lang/en'
// import locale from 'element-plus/lib/local'

const app = createApp(App)
app.use(store)
app.use(router)
app.mount('#app')
