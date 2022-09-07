import axios from "axios";
import { errorCodeType } from "./error-code-type";
import { userStore } from "store/modules/user";
const user = userStore();

var instance = axios.create({
  timeout: 3500,
  baseURL: "http://localhost:5000/api",
  headers: {
    "Content-Type": "application/json;charset=UTF-8;",
  },
});

instance.interceptors.request.use(
  (config: any) => {
    const token = user.token;
    console.log(token);
    token && (config.headers.Authorization = token);
    if (config.methods === "POST") {
      config.data = JSON.stringify(config.data);
    }
    return config;
  },
  (error) => Promise.reject(error)
);

instance.interceptors.response.use(
  (response) => {
    // console.log("响应成功");
    return response.data;
  },
  (error) => {
    console.log("响应错误");
    if (error.response && error.response.status) {
      //   const status = error.response.status;
      return Promise.reject(error);
    }
    return Promise.reject(error);
  }
);

export default instance;
