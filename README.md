# project2-elgomez

## Theme:
The idea I had behind this project was to eventually make it a centralized location for my group of friends to chat. 
We are a group of gamers that play very often across many different games, but our competetive teams are called "the Chicken kickers"
(Disclaimer I did not come up with the name) To make this fit the theme of our grou I added our logo as well as Chicken bot! Chicken bot
has a few commands thus far,which can be seen by using the command !! help.

### Known Problems:
As of now the functionality for Postgres is the most lacking. Upon entering the chat room the user can view the chat history
as well as log in and chat. The issue is that the mapping and navigation of my postgres was a bit off, and because of this it has to be 
put off for this milestone. I am confident that given another day I could get this implemented. 

Another Known issue is the disconnect not removing users from the user list. It works ocassionally, but debugging has proved difficult.
I am sure that there is a more efficient and simple way to do this using reacts componentDidunmount() function, but I had trouble finding
proper documentation on how to use it.

The last known problem is that the page has a scroll bar on some resolutions and not others. on 1080p monitors it does not, yet on some lower resolutuions it does. I thought this would be fixed by using vh in my css file, but there is probably soemthing else that is causing this problem.

#### if possible, I would like to work on the postgres and userlist implementation more and gain back any points that I missed due to these not working as expected.
