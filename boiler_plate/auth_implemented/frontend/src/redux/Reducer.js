const init_user_state = {
    isLoggedIn: false,
    menuLabel: 'Login',
    showRegisterButton: true,
    data: {}
}

const loginReducer = (state = init_user_state, action) => {
    switch(action.type) {
        case 'USER_LOGIN':
            return {
                ...state,
                    isLoggedIn: true,
                    menuLabel: 'Logout',
                    showRegisterButton: false,
                    data: action.payload.data
                }
        case 'USER_LOGOUT':
            return {...state, 
                        isLoggedIn: false,
                        menuLabel: 'Login',
                        showRegisterButton: true,
                        data: {}
                    }
    }
    return state
}

export {loginReducer}