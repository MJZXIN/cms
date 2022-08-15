import { axios } from "../utils/axios/request";

const registry = (data:any) => {
    return axios({
        url: "/registry",
        data
    })
}

const getUser = (data: any) => {
    return axios({
        url: "/getUser",
        data,
        config: {
            headers: {
                'Request': 'phone'
            },
            timeout: 3000
        }
    })
}

export {
    getUser,
    registry
}