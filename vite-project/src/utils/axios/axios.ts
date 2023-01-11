import axios from 'axios'
import { ElMessage } from 'element-plus'

// 创建axios实例
const service = axios.create({
    baseURL: import.meta.env.BASE_URL,
    timeout: 10000 // 请求超时时间
})

// request拦截器
service.interceptors.request.use(
    (config: any) => {
        // if (store.getters.token) {
        // config.headers['X-Token'] = '12222222'// 让每个请求携带自定义token 请根据实际情况自行修改
        // }
        return config
    },
    error => {
        // Do something with request error
        console.log(error) // for debug
        Promise.reject(error)
    }
)

// response 拦截器
service.interceptors.response.use(
    response => {
        /**
         * code为非20000是抛错 可结合自己业务进行修改
         */
        // const res = response.data
        // if (res.code !== 20000) {
        //     Message({
        //         message: res.message,
        //         type: 'error',
        //         duration: 5 * 1000
        //     })
        return response.data
    },
    error => {
        console.log('err' + error) // for debug
        ElMessage({
            message: `网络超时，没有请求到数据`,
            type: 'error',
            duration: 3 * 1000
        })
        return Promise.reject(error)
    }
)
export default service;