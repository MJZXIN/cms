import { axios } from "utils/axios/request";

const getCorp = (page) => {
  return axios({
    method: "get",
    url: "/system/corp/" + page,
  });
};

const addCorp = (form) => {
  return axios({
    method: "post",
    url: "/system/corp",
    data: form,
  });
};

const getDept = (page) => {
  return axios({
    method: "get",
    url: "/system/dept/" + page,
  });
};

const getDeptByCorp = (corp) => {
  return axios({
    method: "get",
    url: "/system/dept?corp=" + corp,
  });
};

const getCorpList = () => {
  return axios({
    method: "get",
    url: "/system/dept/corp",
  });
};

const addDept = (form) => {
  return axios({
    method: "post",
    url: "/system/dept",
    data: form,
  });
};

const getPost = (page) => {
  return axios({
    method: "get",
    url: "/system/post/" + page,
  });
};

const addPost = (form) => {
  return axios({
    method: "post",
    url: "/system/post",
    data: form,
  });
};

const getRole = (page) => {
  return axios({
    method: "get",
    url: "/system/role/" + page,
  });
};

const addRole = (form) => {
  return axios({
    method: "post",
    url: "/system/role",
    data: form,
  });
};

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

export {
  getCorp,
  addCorp,
  getDept,
  addDept,
  getDeptByCorp,
  getCorpList,
  getPost,
  addPost,
  getRole,
  addRole,
  getUser,
  addUser,
};
