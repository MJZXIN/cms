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

const logout = (data: any) => {
  return axios({
    method: "get",
    url: "/logout",
    data,
  });
};

export { login, register, logout };
