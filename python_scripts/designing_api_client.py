
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


"""Еще одна версия"""

from datetime import datetime
import requests
import jwt
import xml.etree.ElementTree as ET


class API:
    def __init__(self, host: str, username: str, password: str):
        self.host = host.rstrip('/')
        self.username = username
        self.password = password
        self.access_token = None
        self.refresh_token = None
        self.data = None

    def __convert_to_xml(self):
        if self.data and isinstance(self.data, dict):
            root = ET.Element("document")
            for key, value in self.data.items():
                ET.SubElement(root, key).text = str(value)
            return ET.tostring(root, encoding="utf-8")
        raise TypeError("Attribute 'data' must be DictType ")

    def __is_token_expired(self):
        if not self.access_token:
            return True
        try:
            payload = jwt.decode(
                self.access_token,
                options={"verify_signature": False}
            )
            exp = payload.get("exp")
            if not exp:
                return True
            return datetime.utcnow() > datetime.utcfromtimestamp(exp)
        except jwt.DecodeError:
            return True

    def __validate_token(self):
        if self.access_token and not self.__is_token_expired():
            return True
        if self.refresh_token:
            try:
                self.refresh()
                return True
            except Exception:
                self.login()
                return True
        return False

    def login(self):
        response = requests.post(
            f"{self.host}/api/auth/login",
            json={"login": self.username, "password": self.password}
        )
        response.raise_for_status()
        data = response.json()
        self.access_token = data.get("access_token")
        self.refresh_token = data.get("refresh_token")

    def refresh(self):
        response = requests.post(
            f"{self.host}/api/auth/refresh",
            json={"refresh_token": self.refresh_token}
        )
        response.raise_for_status()
        data = response.json()
        self.access_token = data.get("access_token")
        self.refresh_token = data.get("refresh_token")

    def get_docs(self):
        if not self.__validate_token():
            raise Exception("Authentication failed")
        response = requests.get(
            f"{self.host}/api/docs",
            headers={"Authorization": f"Bearer {self.access_token}"}
        )
        if response.status_code == 401:
            self.refresh()
            return self.get_docs()
        response.raise_for_status()
        return response.text

    def validate_data(self):
        if not self.__validate_token():
            raise Exception("Authentication failed")

        doc = self.__convert_to_xml()
        response = requests.post(
            f"{self.host}/api/docs/validate",
            data=doc,
            headers={"Content-Type": "application/xml"}
        )
        if response.status_code == 401:
            self.refresh()
            return self.validate_data()
        response.raise_for_status()
        return response.json()







































