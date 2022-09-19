import { axios } from "utils/axios/request";

const getPart = (page) => {
  return axios({
    method: "get",
    url: "/product/part/" + page,
  });
};

const addPart = (form) => {
  return axios({
    method: "post",
    url: "/product/part",
    data: form,
  });
};

export { getPart, addPart };
