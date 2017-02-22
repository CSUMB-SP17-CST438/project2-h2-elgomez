import * as React from 'react';

import { Button } from './Button';

import { Socket } from './Socket';


export class Content extends React.Component {
    
    constructor(props) {
        super(props);
        this.state = {
            'numbers': [],
            'users': [],
        };
        
 }
    componentDidMount() {
        Socket.on('all numbers', (data) => {this.setState({'numbers': data['numbers']});});
        Socket.on('all users', (data) => {this.setState({'users': data['users']});});
         
        FB.getLoginStatus((response) => {if (response.status == 'connected') 
            {
                Socket.emit('new number', {'facebook_user_token':response.authResponse.accessToken,'number': "connected",});
            }
        let auth = gapi.auth2.getAuthInstance();
        let user = auth.currentUser.get();
                
        if (user.isSignedIn()) 
        {
            Socket.emit('new number', {'google_user_token':user.getAuthResponse().id_token,'facebook_user_token': '','number': "connected",});
        }

    });
}

        
    render() {
       
        let numbers = this.state.numbers.map((n, index) =>
           <li key={index}>
                <img src={n.picture} />
                {n.name}: {n.number}
            </li>
        );
         let users = this.state.users.map((n, index) =>
           <li key={index}>
                <img src={n.picture} />
                {n.name}
            </li>
        );

        return (
            
         <div>
             
    
            <h1>
                <div
                    className="fb-login-button"
                    data-max-rows="1"
                    data-size="large"
                    data-show-faces="false"
                    data-auto-logout-link="true">
                </div>
                <div className="g-signin2" data-theme="dark">
                </div>
            </h1>
            
            <h2 color = "White">Chicken Chat!
            </h2>
            
            <input type = "text" id = "message_in">
            </input> 
            
         <Button />
         <ul id = 'myUL3'>
        <ul id = 'myUL'>{numbers}</ul>
        <ul id = 'myUL2'>{users}</ul>
        </ul>
       
      
         </div>
         
         );

    }
    
}