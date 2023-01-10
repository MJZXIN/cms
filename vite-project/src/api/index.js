import request from '../utils/axios';

const Api = process.env.BASE_URL || 'http://localhost:5000';

const getTest = () => {
    return request({
        url: Api + '/testApi/test',
        method: 'get',
    })
}

export {
    getTest
}