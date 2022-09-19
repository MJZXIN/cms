import { axios } from "utils/axios/request";

const getProduct = (page) => {
  return axios({
    method: "get",
    url: "/product/product/" + page,
  });
};

const addProduct = (form) => {
  return axios({
    method: "post",
    url: "/product/product",
    data: form,
  });
};

export { getProduct, addProduct };
