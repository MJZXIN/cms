import request from '../utils/axios';

const getTest = () => {
    
    return request({
        url: '/testApi/test',
        method: 'get',
    })
}

export {
    getTest
}