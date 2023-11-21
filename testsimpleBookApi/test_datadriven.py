# from utils.fileutils import getCsvDataAsDict
# from utils.myutils import postApidata
# baseURI=getFlaskAppBaseURL()
# dataFile='registerApiData.csv'
# urlPath='register'
#
#
# def test_dataDrivenRegApi():
#     url = baseURI + urlPath
#     payloadList = getCsvDataAsDict(dataFile)
#     for dataLines in payloadList:
#         resp = postApidata(url, dataLines)
#         assert resp.status_code == 201
#         data = resp.json()
#         assert data['id']
#
#
import json

import requests


def test_get_data():
    response=requests.get( 'https://simple-books-api.glitch.me/books?type=fiction&limit=0')
    data=response.json()
    print(json.dumps(data,indent=6))