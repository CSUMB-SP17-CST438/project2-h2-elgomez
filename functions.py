import random
import requests
def get_chatbot_response(data):
    botCheck = data
    botHelp = '!! help'
    botAbout= '!! about'
    botSay = '!! say'
    botJoke = '!! joke'
    botCross = '!! cross'
    botRank = '!! rank'
    botMaster = '!! master'
    all_mah_numbers = []
    chickenBotVer = 1
    message = ""
    riotKey = '60512c7b-5391-4678-a7c4-f8b0ab0230cb'
    if botCheck[0:7] == botHelp:
       
        message = ({
            'name': 'ChickenBot ',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': 'Commands: !! help(help message) !! about(about the chatroom) !! say (make me say something: ex!! say <something>) !! joke (I will tell a joke)  !! cross(make me cross the road)' + 
            " !! rank <region> <summonerName>: get the rank of a summoner from league of legends, Example (!! rank na doublelift)."
        })
    elif botCheck[0:7] == botRank:
        spl = str.split(str(data))
        if len(spl) < 4:
            message = ({
            'name': 'ChickenBot ',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': "ERROR: Either no summoner name or Region given"
            })
            return message
        print spl[2] + " " + spl[3]
        region = spl[2]
        summoner = str(spl[3])
        RiotJson = GetSummonerData(region,summoner,riotKey)
        sn = RiotJson[summoner]['name']
        ID = RiotJson[summoner]['id']
        ID = str(ID)
        print ID
        RiotJson2 = GetRankedData(region,ID,riotKey)
        expression = str(RiotJson2[ID][0]['tier'])
        say = ""
        if(expression =="SILVER"):
            say = "trash noob loser"
        if(expression =="GOLD"):
            say = "Moderatley garbage"
        if(expression =="PLATINUM"):
            say = "You think you are better than me?"
        if(expression =="DIAMOND"):
            say = "Whatever xiao"
        if(expression =="MASTER"):
            say = "garbage master elo"
        if(expression =="CHALLENGER"):
            say = "alright whatever man"
        if(expression =="BRONZE"):
            say = "Bottom of the barrel"
        message = ({
            'name': 'ChickenBot ',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': "the summoner: " + sn + " has a rank of " + str(RiotJson2[ID][0]['tier']) + " " + str(RiotJson2[ID][0]['entries'][0]['division']) + " " + say
        })
    # elif botCheck[0:9] == botMaster:
    #     spl = str.split(str(data['number']))
        
    #     region = spl[2]
    #     summoner = str(spl[3])
    #     RiotJson = GetSummonerData(region,summoner,riotKey)
    #     ID = RiotJson[summoner]['id']
    #     ID = str(ID)
    #     RiotJson2 = GetMasteryData(3,ID,riotKey)
    #     print "Champ ID: " + str(RiotJson2[0]['championId'])
    #     champNum1 = str(RiotJson2[0]['championId'])
    #     champNum2 = str(RiotJson2[1]['championId'])
    #     champNum3 = str(RiotJson2[2]['championId'])
        
    #     RiotJson3 = GetChampData(riotKey,champNum1)
       
    #     champ1 = RiotJson3[champNum1]['name'] + RiotJson3[champNum1]['title']
       
        
    #     all_mah_numbers.append({
    #         'name': 'ChickenBot ',
    #         'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
    #         'number': "the summoner: " + summoner + " top played champions are: " + champ1 + ", " + champ2 + " and " + champ3
    #     })
    elif botCheck[0:6] == botSay:
       
        word = botCheck
        message = ({
            'name': 'ChickenBot_version',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': word[6:]
        })
    elif botCheck[0:8] == botAbout:
       
        message = ({
            'name': 'ChickenBot ',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': "hello This is chicken bots chatroom, please do not kick me. This app is used for chatting and stuff I guess, Please refer to this github link for more info: "
        })
    elif botCheck[0:7] == botJoke:
      
        jokes = ['guess what...chickenBot','why did chickenBot cross the road? because chickenBots road crossing function was invoked.','what do you call a fake noodle? An impasta!',
        'What did one plate say to the other?.... Lunch is on me.','Why did the hipster fall in the lake?.....He went ice skating before it was cool.',
        'Why can\'t you trust atoms?....Because they make up everything!']
        
        message = ({
            'name': 'ChickenBot_Version ',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': random.choice(jokes)
        })
    elif botCheck[0:8] == botCross:
    
        r = random.randint(0,1)
        string = ''
        if r == 1:
            string = "ChickenBot made it across safely"
        else:
            string = "I hope you are happy...ChickenBot has perished and I have taken his place"
            
            
        message = ({
            'name': 'ChickenBot_Version ',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': string
        })
    else:
        message = ({
            'name': 'ChickenBot_Version ',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': "unknown command: " + botCheck
        })
    return message
    
def GetSummonerData(region,summonerName,key):
    url = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + key
    response = requests.get(url)
    
    return response.json()
def GetRankedData(region,ID,key):
    url = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + key
    response = requests.get(url)
    print response
    return response.json()
def GetMasteryData(count,ID,key):
    url = "https://na.api.pvp.net/championmastery/location/NA1/player/" + ID + "/topchampions?count=3&api_key=" + key
    response = requests.get(url)
    print response
    return response.json()
def GetChampData(key,id):
    url = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?dataById=true&api_key=60512c7b-5391-4678-a7c4-f8b0ab0230cb"
    response = requests.get(url)
    return response