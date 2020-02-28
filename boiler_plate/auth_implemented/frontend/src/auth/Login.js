import React from 'react'
import axios from 'axios'
import {user_login} from '../redux/Action'
import {connect} from 'react-redux'

class Login extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            username: '',
            password: ''
        }
    }

    handleChange = (event) => {
        this.setState ({
            [event.target.name]: event.target.value
        })
    }

    handleClick = () => {
        
        const url = 'http://localhost:5000/user/login'
        axios.post(url, this.state)
        .then(res => {
            console.log(res['data']['data'])
            this.props.user_login(res['data']['data'])
            this.props.history.push('/')
        })
        .catch(res => {
            console.log(res)
        })
    }

    render() {
        return (
            <div>
                <div className='row mt-2'>
                    <div className='col-7 offset-2'>
                        <h3 className='bg-primary text-white p-3'>Login Here.</h3>
                    </div>
                </div>
                <div className='row mt-4'>
                    <div className='col-2 offset-2'>Username</div>
                    <div className='col-5'>
                        <input name="username" onChange={this.handleChange} value={this.state.username} type='text' placeholder = 'Enter Username' className='form-control'></input>
                    </div>
                </div>
                <div className='row mt-2'>
                    <div className='col-2 offset-2'>Password</div>
                    <div className='col-5'>
                        <input name="password" onChange={this.handleChange} value={this.state.password} type='password' placeholder = 'Enter Password' className='form-control'></input>
                    </div>
                </div>
                <div className='row mt-3'>
                    <div className='col-7 offset-2'>
                        <button onClick={this.handleClick} className='btn btn-primary form-control'>Login</button>
                    </div>
                </div>
            </div>
        )
    }    


}


const mapDispatchToProps = (dispatch) => {
    return {
        user_login: (data) => dispatch(user_login(data))
    }
}

export default connect(null, mapDispatchToProps)(Login) 

// export default Login