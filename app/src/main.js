import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import * as ElIcons from "@element-plus/icons-vue";
import { ElMessage, ElMessageBox } from "element-plus";
import router from "./router";
import axios from "axios";
import store from "./store";

const app = createApp(App);
for (const name in ElIcons) {
  app.component(name, ElIcons[name]);
}
app.config.globalProperties.$axios = axios;
app.config.globalProperties.$message = ElMessage;
app.config.globalProperties.$mesbox = ElMessageBox;

app.use(router);
app.use(store);
app.mount("#app");
