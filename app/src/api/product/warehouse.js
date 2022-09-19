import { axios } from "utils/axios/request";

const getWarehouse = (page) => {
  return axios({
    method: "get",
    url: "/product/whsh/" + page,
  });
};

const getWarehouseByCorp = (corp) => {
  return axios({
    method: "get",
    url: "/product/whsh?corp=" + corp,
  });
};

const addWarehouse = (form) => {
  return axios({
    method: "post",
    url: "/product/whsh",
    data: form,
  });
};

export { getWarehouse, getWarehouseByCorp, addWarehouse };
