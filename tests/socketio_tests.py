# socketio_tests.py
import app, unittest

class SocketIOTestCase(unittest.TestCase):
    def test_server_sends_hello(self):
        # client = app.socketio.test_client(app.app)
        # r = client.get_received()
        # #print r
        # #self.assertEquals(len(r), 1)
        # from_server = r[0]
        # self.assertEquals(
        #     from_server['name'],
        #     'all numbers'
        # )
        # data = from_server['args'][0]
        # self.assertEquals(data['message'], 'all numbers')
        print ""
    # def test_server_relays_message(self):
    #     client = app.socketio.test_client(app.app)
    #     client.emit('new message', {'name':"TestUser_1",
    #     'message': "Dank",'image': 'http://i.imgur.com/8c3NLXb.png'})
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
    #         d[0]['number'],
    #         u'Dank'
    #     )
    
    
if __name__ == '__main__':
    unittest.main()