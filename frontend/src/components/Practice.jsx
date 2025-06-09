import React from 'react';


class Count extends React.Component{
    constructor(props){
        super()
        this.state = {
            count:0
        }
    }

    increment = () =>{
        this.setState(
            (prev) => (
                {count: prev.count + 1}
            )
        )
    }
    render(){
        return(
            <div>
                <h3>Hello world</h3>
                <p>Welcome to class component.</p>
                <p>Count: {this.state.count}</p>
                <button onClick={this.increment}>Increase</button>
            </div>
        )
    }
}

export default Count