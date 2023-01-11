import { MockMethod } from 'vite-plugin-mock'

export default [
  {
    url: "/api/mock/testApi/test",
    method: "get",
    response: () => {
      return {
        code: 200,
        message: "ok",
        data: ["tom", "jerry"]
      };
    }
  }
] as MockMethod[]