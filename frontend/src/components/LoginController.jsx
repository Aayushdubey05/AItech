import React, { Component } from "react";
import LoginButton from "../buttons/LoginButton";
import LogoutButton from "../buttons/logoutbutton";

export default class LoginController extends Component{

    constructor(props){
        super(props);
        this.handleLoginConnector = this.handleLogin.bind(this)
        this.handleLogoutConnector = this.handleLogout.bind(this)
        this.state = {isloggedin:false}
    }


    handleLogin(){
        this.setState({isloggedin:true})
    }

    handleLogout(){
        this.setState({isloggedin:false})
    }

    render(){
        const isLoggedin = this.state.isloggedin;
        let button
        if(isLoggedin){
            button = <LogoutButton onClick={this.handleLogoutConnector}></LogoutButton>
        }
        else{
            button = <LoginButton onClick={this.handleLoginConnector}></LoginButton>
        }

        return(
            <div>
                {button}
            </div>
        )
    }
}