import pytest
from utils.fileutils import getjsonFromFile
from utils.myconfigparser import getPetApiURL
from utils.myutils import getApiData, postApidata


LoginJsonFile = 'registerApiValid.json'
baseURI = getPetApiURL()
loginURLPath = '/api-clients'


@pytest.fixture
def get_token():
    loginurl = baseURI + loginURLPath
    payload = getjsonFromFile (LoginJsonFile)
    resp = postApidata(loginurl,payload)

    print(resp.json()['token'])
    token = resp.json()['token']
    yield token
