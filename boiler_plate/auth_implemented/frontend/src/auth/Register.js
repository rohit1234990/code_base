import React from 'react'
import axios from 'axios'
import {connect} from 'react-redux'


class Register extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            name: '',
            email: '',
            username: '',
            password: ''
        }
    }


    handleSignup = () => {
        const url = 'http://localhost:5000/user/register'
        axios.post(url, this.state)
        .then(res => {
            if (res['data']['result'] === 'success') {
                this.props.history.push('/login')
                // console.log('success')
            } 
        })
        .catch(res => {
            console.log(res)
        })
    }

    handleChange = (event) => {
        this.setState({
            [event.target.name]: event.target.value
        })
        // console.log(this.state)
    }

    render() {
        return (
            <div>
                <div className='row mt-2'>
                    <div className='col-7 offset-2'>
                        <h3 className='bg-primary text-white p-3'>Signup Here.</h3>
                    </div>
                </div>
                <div className='row mt-3'>
                    <div className='col-2 offset-2'>Name</div>
                    <div className='col-5'>
                        <input name="name" onChange={this.handleChange} value={this.state.name} type='text' placeholder='Enter Name' className='form-control'></input>
                    </div>
                </div>
                <div className='row mt-2'>
                    <div className='col-2 offset-2'>Email</div>
                    <div className='col-5'>
                        <input name="email" onChange={this.handleChange} value={this.state.email} type='text' placeholder = 'Enter Email' className='form-control'></input>
                    </div>
                </div>
                <div className='row mt-2'>
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
                        <button onClick={this.handleSignup} className='btn btn-primary form-control'>Sign Up</button>
                    </div>
                </div>
            </div>
        )
    }
    
}

/*
const mapDispatchToProps = (dispatch) => {
    return {
        user_logout: () => dispatch(user_logout())
    }
}

export default connect(null, mapDispatchToProps)(Register)
*/

export default Register