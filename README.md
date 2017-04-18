# project2-elgomez

## Theme:
The idea I had behind this project was to eventually make it a centralized location for my group of friends to chat. 
We are a group of gamers that play very often across many different games, but our competetive teams are called "the Chicken kickers"
(Disclaimer I did not come up with the name) To make this fit the theme of our grou I added our logo as well as Chicken bot! Chicken bot
has a few commands thus far,which can be seen by using the command !! help. To better fit the theme My bot now implements a !! rank command. Gloating within a team chatroom is always welcome and with the !! rank command one can look up the rank of any person who plays the game League of legends using their api. I believe this command fits the theme of a "team based gaming chat" by allowing users to look up statistics on their fellow teammates with simple command.

### Known Problems:
As of now the functionality for Postgres is the most lacking. Upon entering the chat room the user can view the chat history
as well as log in and chat. The issue is that the mapping and navigation of my postgres was a bit off, and because of this it has to be 
put off for now. 

Another Known issue is the disconnect not removing users from the user list. It works ocassionally, but debugging has proved difficult.
I am sure that there is a more efficient and simple way to do this using reacts componentDidunmount() function, but I had trouble finding
proper documentation on how to use it.

Some images work in terms of size when rendered in a message, yet others are too large. Dynamically changing the images render size would be ideal, yet I had trouble finding a way to do this without rendering a box when the message was not an image.

One more issue is that of transperancy with the chat menu and the background. When a message is an image rendered in line the background can be a bit distracting due to the transperency given to the div element that the user messages are housed in.

The last known problem is that the page has a scroll bar on some resolutions and not others. on 1080p monitors it does not, yet on some lower resolutuions it does. I thought this would be fixed by using vh in my css file, but there is probably soemthing else that is causing this problem.

###Possible future imporvements
More functionallity with the league of legends API. The league api is a very powerful tool that can get stats and references to in game objects as well as give links to replays of matches and give a link to view a featured match through their spectate function.

Postgres and the user list are the most pressing improvements. By making these function with more consistancy the reliability and overall user experience would be much higher.
#### Link To Heroku Deployment
