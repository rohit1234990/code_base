import React from 'react'

class TaskList extends React.Component {
    constructor(props) {
        super(props) 
        this.state = {

        }
    }

    render() {
        return (
            <div className='card'>
                <div className='card-header'>
                    <h3>TaskList #</h3>
                </div>
                <div className='card-body'>
                    <h5>Heading for list</h5>
                    <table className='table'>
                        <thead>
                            <tr>
                                <th>S.No</th>
                                <th>Task Name</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1. </td>
                                <td>First ever task </td>
                                <td>delete</td>
                            </tr>
                        </tbody>
                        <tfoot>
                            <tr>
                                <td>1. </td>
                                <td>
                                    <textarea className='form-control row=2'></textarea>
                                </td>
                                <td>add</td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
            </div>
        )
    }
}

export default TaskList