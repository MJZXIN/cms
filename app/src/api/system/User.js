import { axios } from "utils/axios/request";

const getUser = (page) => {
  return axios({
    method: "get",
    url: "/system/user/" + page,
  });
};

const addUser = (form) => {
  return axios({
    method: "post",
    url: "/system/user",
    data: form,
  });
};

export { getUser, addUser };
