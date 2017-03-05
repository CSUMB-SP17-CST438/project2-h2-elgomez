# socketio_tests.py
import app, unittest

class SocketIOTestCase(unittest.TestCase):
    def test_server_sends_hello(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        print r
        self.assertEquals(len(r), 1)
        from_server = r[0]
        self.assertEquals(
            from_server['name'], 
            'hello to client'
        )
        data = from_server['args'][0]
        self.assertEquals(data['message'], 'Hey there!')
    def test_server_relays_message(self):
        client = app.socketio.test_client(app.app)
        client.emit('new number', {'facebook_user_token':"EAAFafAD7IK8BAIXNkJWxjqYoge9fQ9scWJ3Fphir9E1DxpVKS4B4rJaOPXFAxYeiJRSj6FSVKKnEZCCbIXZCXf0UzaTmiF7VuyphM8pGBZB3ZCr5a2mmjw9CAoswiRb0Jc6cBoYqIrE5q1ZBVT6stQ5VeM2c1eXr7OVTSzVzq1eX7SqSZCRWmxDPgThmf4on0ZD",
        'number': "Dank",})
        r = client.get_received()
       
        
        from_server = r[1]
        self.assertEquals(
            from_server['name'],
            'all numbers'
        )
        data1 = from_server['args'][0]
        #print data1['numbers']
        d = data1['numbers']
        self.assertEquals(
            d[0]['number'],
            u'Dank'
        )
    def test_server_relays_Image(self):
        client = app.socketio.test_client(app.app)
        client.emit('new number', {'facebook_user_token':"EAAFafAD7IK8BAIXNkJWxjqYoge9fQ9scWJ3Fphir9E1DxpVKS4B4rJaOPXFAxYeiJRSj6FSVKKnEZCCbIXZCXf0UzaTmiF7VuyphM8pGBZB3ZCr5a2mmjw9CAoswiRb0Jc6cBoYqIrE5q1ZBVT6stQ5VeM2c1eXr7OVTSzVzq1eX7SqSZCRWmxDPgThmf4on0ZD",
        'number': "Dank",})
        r = client.get_received()
       
        
        from_server = r[1]
        self.assertEquals(
            from_server['name'],
            'all numbers'
        )
        data1 = from_server['args'][0]
        #print data1['numbers']
        d = data1['numbers']
        self.assertEquals(
            d[0]['picture'],
            u'https://scontent.xx.fbcdn.net/v/t1.0-1/p50x50/14212660_1143635145684521_8926022275418377810_n.jpg?oh=12b0b03c18538bc1d24c3b271a9abb53&oe=593C4AD7'
        )
    # def test_server_relays_Connected(self):
    #     client.emit('new number', {'facebook_user_token':"EAAFafAD7IK8BAIXNkJWxjqYoge9fQ9scWJ3Fphir9E1DxpVKS4B4rJaOPXFAxYeiJRSj6FSVKKnEZCCbIXZCXf0UzaTmiF7VuyphM8pGBZB3ZCr5a2mmjw9CAoswiRb0Jc6cBoYqIrE5q1ZBVT6stQ5VeM2c1eXr7OVTSzVzq1eX7SqSZCRWmxDPgThmf4on0ZD",
    #     'number': "Dank",})
    #     r = client.get_received()
       
        
    #     from_server = r[1]
    #     self.assertEquals(
    #         from_server['name'],
    #         'all numbers'
    #     )
    #     data1 = from_server['args'][0]
    #     #print data1['numbers']
    #     d = data1['numbers']
    #     self.assertEquals(
    #         d[0]['picture'],
    #         u'https://scontent.xx.fbcdn.net/v/t1.0-1/p50x50/14212660_1143635145684521_8926022275418377810_n.jpg?oh=12b0b03c18538bc1d24c3b271a9abb53&oe=593C4AD7'
    #     )
    
    
if __name__ == '__main__':
    unittest.main()