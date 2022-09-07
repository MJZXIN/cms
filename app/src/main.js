import { createApp } from "vue";
import "./style.css";
import "@/assets/style.css";
import App from "./App.vue";
import * as ElIcons from "@element-plus/icons-vue";
import { ElMessage, ElMessageBox } from "element-plus";
import axios from "axios";
import store from "./store";
import router from "./router";

const app = createApp(App);
for (const name in ElIcons) {
  app.component(name, ElIcons[name]);
}
app.config.globalProperties.$axios = axios;
app.config.globalProperties.$message = ElMessage;
app.config.globalProperties.$mesbox = ElMessageBox;

app.use(store);
app.use(router);

app.mount("#app");
