import { axios } from "../utils/axios/request";

const login = (data: any) => {
  return axios({
    method: "post",
    url: "/login",
    data,
  });
};

const register = (data: any) => {
  return axios({
    method: "post",
    url: "/reg",
    data,
  });
};

const getMenu = () => {
  return axios({
    method: "get",
    url: "/menu",
  });
};

const getUser = (data: any) => {
  return axios({
    url: "/getUser",
    data,
    config: {
      headers: {
        Request: "phone",
      },
      timeout: 3000,
    },
  });
};

export { login, getUser, register, getMenu };
