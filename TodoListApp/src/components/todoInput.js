import React from 'react';
import './todoInput.css';



export default class TodoInput extends React.Component{
    constructor(props){
        super(props)

        this.state = {value: ""};

        this.handleChange = this.handleChange.bind(this);
        this.addTodo = this.addTodo.bind(this);
        this.handleKeyPress = this.handleKeyPress.bind(this);
    }
        handleChange(e) {
          this.setState({value:e.target.value})
        }
        handleKeyPress(e){
            if (e.key == 'Enter'){
                //alert("Enter Pressed")
                //console.log(e)
                this.addTodo(this.state.value)

            }
        }
        onClickSubmit = () => {
            this.addTodo(this.state.value)
        }


        addTodo(todo) {
            if (todo.length>0){
                this.props.addTodo(todo); 
                this.setState({value: ''})

            }         
        }


    
    render(){
        return(
            <div> 
                <input type="text" value={this.state.value} onChange={this.handleChange} placeholder='Enter the next To do List Item' onKeyPress={this.handleKeyPress}/>
                <button className="btn btn-primary" onClick={this.onClickSubmit}>Submit</button>
            </div>
        )
    }
}
