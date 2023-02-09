import request from '../utils/axios';
import { getUserByPage } from './System/user'

const login = (params) => {
    
    return request({
        url: '/login',
        method: 'post',
        data: {
            "username": params.username,
            "password": params.password
        }
    })

}

export {
    login,
    getUserByPage
}