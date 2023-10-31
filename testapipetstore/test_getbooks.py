import requests

from utils.myconfigparser import getPetApiURL

from utils.fileutils import getjsonFromFile
from utils.myutils import *
from utils.apiutils import postapiData
# import logging

import pytest

path = '/books/:{bookid:2}'
# logger = logging.getLogger(__name__)
baseURI = getPetApiURL()
URLPATH = '/books?type=fiction&limit=0'
order = '/orders'

registerjsonfile = 'registerApiValid.json'


def test_getAllBooks():
    url = baseURI + URLPATH
    data, resp_status, timeTaken = getApiData(url)

    print(data)
    assert data[0]['id'] == 1
    assert data[2]['name'] == 'The Midnight Library'
    assert resp_status == 200
    assert timeTaken <= 4
    print("Time Taken:", timeTaken)


def test_getSingleBook():
    url = baseURI + path
    data, resp_status, timeTaken = getApiData(url)

    print(data)
    assert data[0]['id'] == 1
    assert data[2]['name'] == 'The Midnight Library'
    assert resp_status == 200
    assert timeTaken <= 2
    print("Time Taken:", timeTaken)


def test_PlaceOrder(get_token):
    token = get_token
    url = baseURI + order
    payload = {'id': 6, 'customerName': 'kiran'}
    headers = {"content-Type": "application/json", "x-access-token": token}
    data, resp_status, timeTaken = postApidata(url, payload, headers)
    print(data)
    assert data["created"] == 'true'
    assert resp_status == 201
