import os
import flask
import flask_socketio
import requests
import random
from rfc3987 import parse
import functions
import links


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

all_users = []
all_mah_numbers = []
riotKey = '60512c7b-5391-4678-a7c4-f8b0ab0230cb'

@app.route('/')
def hello():

    return flask.render_template('index.html',count = len(all_users))

@socketio.on('connect')
def on_connect():
    socketio.emit('all numbers', {'numbers': all_mah_numbers})
    socketio.emit('hello to client', {
        'message': 'Hey there!'
    })

    
@socketio.on('disconnect')
def on_disconnect():
    print "someone disconnected"
    all_mah_numbers.append({
            'name': 'ChickenBot '+ str(chickenBotVer),
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': "A user disconnected"
        })
    socketio.emit('all numbers', {'numbers': all_mah_numbers})
    socketio.emit('all users', {'users': all_users})
    
    
@socketio.on('user_Count')
def userCount():
    global all_users
    count = len(all_users)
    return count
    


chickenBotVer = 1

   
@socketio.on('new message')
def on_new_message(data):
    socketio.emit('got your message', {
        'your message': data['my message']
    })

@socketio.on('new number')
def on_new_number(data):
    response = requests.get('https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])
    json = response.json()
    
    global chickenBotVer
    check = True
    ##connected user messages--------------------------------------------------------------------------------------------------------------------------------------------
    if(data['number'] == "connected"):
        if(data['facebook_user_token'] != ''):
            check = True
            for key in all_users:
            
                if key['name'] == json['name']:
                    check = False
                    socketio.emit('all users', {'users': all_users})
                 
            
            all_mah_numbers.append({
                'name': 'ChickenBot '+ str(chickenBotVer),
                'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
                'number':json['name'] + " " + data['number']
            })
            socketio.emit('all numbers', {'numbers': all_mah_numbers})
            
            if check == True:
                all_users.append({
                    'name': json['name'],
                    'picture': json['picture']['data']['url'],
                })
                
            socketio.emit('all users', {'users': all_users})
        
        elif(data['facebook_user_token'] == ''):
            response2 = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])
            json2 = response2.json()
            check = True
            for key in all_users:
            
                if key['name'] == json['name']:
                    print "name" + key
                    check = False
                    socketio.emit('all users', {'users': all_users})
                     
                
                all_mah_numbers.append({
                    'name': 'ChickenBot '+ str(chickenBotVer),
                    'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
                    'number':json2['name'] + " " + data['number']
                })
            socketio.emit('all numbers', {'numbers': all_mah_numbers})
        
            if check == True:
                all_users.append({
                    'name': json2['name'],
                    'picture': json2['picture']
                })
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       
        
            
## APPEND Facebook user message to list---------------------------------------------------------------------------------------------------------------------------------------------
    elif (data['number'] != "connected"):
        
        if data['facebook_user_token'] != '':
            if links.checkURL(data['number']):
                t1 = links.isImage(data['number'])
                print t1
                if t1 == True:
                    all_mah_numbers.append({
                        'name': json['name'],
                        'picture': json['picture']['data']['url'],
                        'number': "",
                        'link': "",
                        'picL': data['number']
                    })
                else:
                    all_mah_numbers.append({
                            'name': json['name'],
                            'picture': json['picture']['data']['url'],
                            'number': "",
                            'link': data['number'],
                            
                        })
            else:
                all_mah_numbers.append({
                        'name': json['name'],
                        'picture': json['picture']['data']['url'],
                        'number': data['number'],
                        'link': "",
                       
                    })
        elif data['facebook_user_token'] == '' :
            t = links.checkURL(data['number'])
            print "**********************************" + str(links.checkURL(data['number']))
            
            if links.checkURL(data['number']):
                t1 = links.isImage(data['number'])
                print t1
                if t1 == True:
                    response2 = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])
                    json2 = response2.json()
                    print "**********************************************************************************" + data['number']
                    all_mah_numbers.append({
                        'name': json2['name'],
                        'picture': json2['picture'],
                        'number': "",
                        'link': "",
                        'picL': data['number']
                    })
                else:
                    response2 = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])
                    json2 = response2.json()
                    all_mah_numbers.append({
                        'name': json2['name'],
                        'picture': json2['picture'],
                        'number': "",
                        'link': data['number'],
                        'n.picL': ""
                    })
            else:
                response2 = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])
                json2 = response2.json()
                all_mah_numbers.append({
                    'name': json2['name'],
                    'picture': json2['picture'],
                    'number': data['number'],
                    'link': "",
                    'n.picL': ""
                })
        
##---------------------------------------------------------------------------------------------------------------------------------------------
    socketio.emit('all numbers', {'numbers': all_mah_numbers})
    socketio.emit('all users', {'users': all_users})
###Bot functionality --------------------------------------------------------------------------------------------------------------------------
    spl = str.split(str(data['number']))
   
    if(spl[0] == "!!"):
        all_mah_numbers.append(functions.get_chatbot_response(data['number']))
###------------------------------------------------------------------------------------------------------------------------------------------- 
    socketio.emit('all numbers', {'numbers': all_mah_numbers})
    socketio.emit('all users', {'users': all_users})

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

