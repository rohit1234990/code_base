import { loginReducer } from "./Reducer"
import {createStore} from 'redux'

const store = createStore(loginReducer)
store.subscribe(() => {
    console.log('redux state : ', store.getState())
})

export default store