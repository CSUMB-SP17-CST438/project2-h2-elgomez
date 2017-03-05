import unittest
import os
import functions

jokes = ['guess what...chickenBot','why did chickenBot cross the road? because chickenBots road crossing function was invoked.','what do you call a fake noodle? An impasta!',
        'What did one plate say to the other?.... Lunch is on me.','Why did the hipster fall in the lake?.....He went ice skating before it was cool.',
        'Why can\'t you trust atoms?....Because they make up everything!']
help =  ({
        'name': 'ChickenBot ',
        'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
        'number': 'Commands: !! help(help message) !! about(about the chatroom) !! say (make me say something: ex!! say <something>) !! joke (I will tell a joke)  !! cross(make me cross the road)' + 
        " !! rank <region> <summonerName>: get the rank of a summoner from league of legends, Example (!! rank na doublelift)."
    })
say = ({
        'name': 'ChickenBot_version',
        'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
        'number': " dang dude"
    })
blank = ({
        'name': 'ChickenBot_version',
        'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
        'number': ""
    })
about = ({
        'name': 'ChickenBot ',
        'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
        'number': "hello This is chicken bots chatroom, please do not kick me. This app is used for chatting and stuff I guess, Please refer to this github link for more info: "
    })
potato =  ({
        'name': 'ChickenBot_Version ',
        'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
        'number': "unknown command: !! Potato"
    })
annie = ({
            'name': 'ChickenBot ',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': "the summoner: Annie Bot has a rank of MASTER I garbage master elo"
        })
doublelift = ({
            'name': 'ChickenBot ',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': "the summoner: Doublelift has a rank of CHALLENGER I alright whatever man"
        })
cross1 = ({
            'name': 'ChickenBot_Version ',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': "I hope you are happy...ChickenBot has perished and I have taken his place"
        })
cross2 = ({
            'name': 'ChickenBot_Version ',
            'picture': 'https://cdn4.iconfinder.com/data/icons/social-productivity-line-art-5/128/chatbot-128.png',
            'number': "ChickenBot made it across safely"
        })
class ChatBotResponseTest(unittest.TestCase):
 
    def test_not_command(self):
        response = functions.get_chatbot_response('!! Potato')
        self.assertEquals(response, potato)
    def test_say_command(self):
        response = functions.get_chatbot_response('!! say dang dude')
        self.assertEquals(response, say)
    def test_say_blank(self):
        response = functions.get_chatbot_response('!! say')
        self.assertEquals(response, blank)
    def test_help(self):
        response = functions.get_chatbot_response('!! help')
        self.assertEquals(response,help)
    def test_Rank_region(self):
        response = functions.get_chatbot_response('!! rank na anniebot')
        self.assertEquals(response,annie)
    def test_Rank_No_region(self):
        response = functions.get_chatbot_response('!! rank anniebot')
        self.assertEquals(response['number'],"ERROR: Either no summoner name or Region given")
    def test_Rank_region2(self):
        response = functions.get_chatbot_response('!! rank na doublelift')
        self.assertEquals(response,doublelift)
    def test_about(self):
        response = functions.get_chatbot_response('!! about')
        self.assertEquals(response,about)
    def test_Cross(self):
        response = functions.get_chatbot_response('!! cross')
        if(response == cross1):
            self.assertEquals(response,cross1)
        elif(response == cross2):
            self.assertEquals(response,cross2)
        else:
            self.assertEquals(response,"")
    def test_joke(self):
        response = functions.get_chatbot_response('!! joke')
        for i in jokes:
            if str(response['number']) == str(i):
               k = i
        self.assertEqual(str(response['number']), k)
            
        
if __name__ == '__main__':
    unittest.main()