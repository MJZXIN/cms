import axios from 'axios'
import { ElMessage } from 'element-plus'
import { userStore } from '@/store'

// 创建axios实例
const service = axios.create({
    baseURL: import.meta.env.VITE_USE_MOCK == 'true' ? import.meta.env.VITE_MOCK_URL : import.meta.env.VITE_BASE_URL,
    timeout: 5000 // 请求超时时间
})

// 暂时禁用axios拦截器
// request拦截器
service.interceptors.request.use(
    (config: any) => {
        const userInfo = userStore()

        if (userInfo.token) {
            config.headers['Authorization'] = userInfo.token// 让每个请求携带自定义token 请根据实际情况自行修改
        }
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
        // TODO: 后续可以启动消息通知
        // ElMessage({
        //     message: `网络超时，没有请求到数据`,
        //     type: 'error',
        //     duration: 3 * 1000
        // })
        return Promise.reject(error)
    }
)
export default service;