import unittest

from app import app

class FlaskappTests(unittest.TestCase):
    def setUp(self):

        self.app = app.test_client()

        # catch exception
        self.app.testing = True

    # GET /api/v1/info
    def test_api_status_code(self):
        result = self.app.get('/api/v1/info')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    # GET /api/users/1
    def test_users_status_code_get(self):
        result = self.app.get('/api/v1/users/1')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)


    # PUT /api/v1/users/1
    def test_users_status_code_put(self):
        result = self.app.put('/api/v1/users/1', data='{"password": "123456"}', content_type='application/json')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    # POST /api/v1/users
    def test_users_status_code_post(self):
        result = self.app.post('/api/v1/users', data='{"username": "xxxx", "email": "1wwww10@qq.comss", \
            "password": "123456222"}', content_type='application/json')
        # assert the status code of the response
        self.assertEqual(result.status_code, 201)

    # DELETE /api/v1/users
    def test_users_status_code_delete(self):
        result = self.app.delete('/api/v1/users', data='{"username": "xxxx"}', content_type='application/json')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    # GET /api/v2/tweets
    def test_tweets_status_code_get(self):
        result = self.app.get('/api/v2/tweets')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    # POST /api/v2/tweets
    def test_tweets_status_code_post(self):
        result = self.app.post('/api/v2/tweets', data='{"username": "yeshan333", "body": "wocoa"}', content_type='application/json')
        # assert the status code of the response
        self.assertEqual(result.status_code, 201)