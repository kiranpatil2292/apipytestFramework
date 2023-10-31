from utils.myconfigparser import getPetApiURL
from utils.apiutils import *
baseURI = getPetApiURL()
URLPATH = '/books?type=fiction&limit=0'
registerjsonfile = 'registerApiValid.json'
petID = '1'
from utils.fileutils import getjsonFromFile
from utils.myutils import *
import pytest
import logging
logger = logging.getLogger(__name__)






def test_getpetById_response():
    url = baseURI + URLPATH
    data, resp_status, timeTaken = getApiData(url)
    logger.info('api testing')

    print(data)
    assert data[1]['name'] == 'The Vanishing Half'
    assert data[0]['type'] == 'fiction'
    assert data[3]['available'] == True
    assert resp_status == 200
    assert timeTaken < 1.4
    print("Time Taken:", timeTaken)


def test_updatingPets():
    payload = {'id': int(petID), 'name': 'cutile', 'status': 'pend'}
    data, resp_status, timeTaken = putdata(baseURI, payload)
    assert data['id'] == int(petID)

# def test_deletepetbyid():
#     url = baseURI + petID
#     apikey = {'api_key': 'apikeys123'}
#     data, resp_status, timeTaken = deletedata(url, apikey)
#     print(data)
#     assert data['message'] == petID
#     assert data['code'] == 200

# testdata=[('application/json',200),
#            ('application/xml',406),
#            ('multipart/mixed',200),
#             ('text/html',406)]
#
# @pytest.mark.parametrize('type,status', testdata)
# def test_getApiusercount(type, status):
#         url = baseURI + URLPATH
#
#     headers = {'accept': type}
#     resp = getApiData(url, headers)
#     print(resp.status_code)
#     assert resp.status_code == status
