const user_login = (data) => {
    return {
        type: 'USER_LOGIN',
        payload: {'data': data}
    }
}

const user_logout = () => {
    return {
        type: 'USER_LOGOUT'
    }
}


export {user_login, user_logout}