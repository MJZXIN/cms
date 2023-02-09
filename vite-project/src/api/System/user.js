import request from 'utils/axios';

const getUserByPage = (page, page_size) => {
    return request({
        url: '/user/' + page + "/" + page_size,
        method: 'get'
    })

}

export {
    getUserByPage
}