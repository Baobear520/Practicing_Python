
# Есть стороннее api
# POST /api/auth/login - на вход логин и пароль на выход JWT и refresh token
# POST /api/auth/refresh - обновить JWN через refresh-токен
# GET /api/docs - получить список документов в формате XML
# POST /api/docs/validate - проверить документ на корректность данных

import requests
from datetime import datetime, UTC


class MyApiClient:

    def __init__(self,username, password, host):
        self.username = username
        self.password = password
        self.host = host
        self.access_token = None
        self.refresh_token = None


    def __is_token_expired(self):
        ...
        token_lifetime = 123 # parse from a JWT token
        return datetime.now(UTC) > datetime.fromtimestamp(token_lifetime,UTC)



    def login(self):
        response =  requests.post(
            url=self.host + '/api/auth/login',
            json={'username': self.username, 'password': self.password}
        )
        json_data = response.json()
        self.access_token, self.refresh_token = json_data.get('access_token'), json_data.get('refresh_token')


    def refresh_login(self):
        response = requests.post(
            url=self.host + '/api/auth/refresh',
            json={'refresh_token': self.refresh_token}
        )
        json_data = response.json()
        self.access_token, self.refresh_token = json_data.get('access_token'), json_data.get('refresh_token')


    def __ensure_token_is_valid(self):
        if self.access_token is not None:
            if self.__is_token_expired():
                self.refresh_login()
        else:
            self.login()


    def get_docs(self):
        self.__ensure_token_is_valid()
        response =  requests.get(
            url=self.host + '/api/docs',
            headers={'authorize': self.access_token})
        response.raise_for_status()
        return response.json()


api_client = MyApiClient(
    username='johndoe',
    password='123',
    host='http://somehost.com'
)
docs = api_client.get_docs()
# тут долго ждали
docs = api_client.get_docs()








