# socketio_tests.py
import app, unittest

googleToken = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImMxYTlmMGNhZjcwNDE0MmExNzIzODQ0YWI1ZjBjOTUxNzBhODNmYzMifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiaWF0IjoxNDg4NzQyMTk4LCJleHAiOjE0ODg3NDU3OTgsImF0X2hhc2giOiJULU9STkZjajdveWZadDlfbjkyREtRIiwiYXVkIjoiMzIzMDQ1OTYzNDM5LXQ3dGYwNWxnYWU2b3JoajlsNGRqb2duZWZoZnAzczNoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAwNTc4MTI2OTIxMjI5MzcyMjAxIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF6cCI6IjMyMzA0NTk2MzQzOS10N3RmMDVsZ2FlNm9yaGo5bDRkam9nbmVmaGZwM3MzaC5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImVtYWlsIjoiZWxpYXMuZi5nb21lekBnbWFpbC5jb20iLCJuYW1lIjoiRWxpYXMgR29tZXoiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tLy1WdEVpdXJidHN1QS9BQUFBQUFBQUFBSS9BQUFBQUFBQUFCYy9WLWRCN21mLVF5dy9zOTYtYy9waG90by5qcGciLCJnaXZlbl9uYW1lIjoiRWxpYXMiLCJmYW1pbHlfbmFtZSI6IkdvbWV6IiwibG9jYWxlIjoiZW4ifQ.SYqYQUDdguB-4ChvZJ96hpx3Nf5_QFw7x1e4q4d0Qd3sTmXd7zoquV-3AK5D8ty8R5628auIppo5IEFjJCTDXrJg2iYNw3NQAGniaig_uY7s6Q_urrhvWQy-NzLRCP7rk8qKyQPRbwg2XL3pDJHcQmURlzUx8tTlJUGp5MySeF9sVgRrxf6xLxGRT98ZFqb0YRJQfY8dFoUB1NNci5ooJerWqp1KaolI0ROU7ERJ-MPuIYAY7yr0GaBfz7RTN5EcKdYJxqlZz2OPSTLNr2AMrJp1kvzH9tZ1bnCQixXa3D2MCp7f23wvUYhs-xKwC9lBnIvJOQdGIhVd0MUJqemJKA'
class SocketIOTestCase(unittest.TestCase):
    def test_server_sends_hello(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        #print r
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
        client.emit('new message', {'name':"TestUser_1",
        'message': "Dank",'image': 'http://i.imgur.com/8c3NLXb.png'})
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
    
    
if __name__ == '__main__':
    unittest.main()