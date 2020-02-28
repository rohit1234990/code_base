import React from 'react'
import TaskList from '../components/TaskList'

class Dashboard extends React.Component {
    constructor(props) {
        super(props)
        this.state = {

        }
    }

    render() {
        return (
            <>
                <TaskList />
            </>
        )
    }
}

export default Dashboard