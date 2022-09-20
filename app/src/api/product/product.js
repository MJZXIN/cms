import { axios } from "utils/axios/request";

const getProduct = (page) => {
  return axios({
    method: "get",
    url: "/product/prod/" + page,
  });
};

const addProduct = (form) => {
  return axios({
    method: "post",
    url: "/product/prod",
    data: form,
  });
};

export { getProduct, addProduct };
