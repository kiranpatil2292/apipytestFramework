import requests


def getApiData(url):
    headers = {'content-Type': 'application/json'}
    response = requests.get(url,verify= False, headers=headers)
    data = response.json()
    assert len(data) > 0, 'empty response'
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


def postApidata(url, body):
    headers = {'content_Type': 'application/json'}
    print('requesturl:', url)
    response = requests.post(url, json=body, headers=headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


def putdata(url, body):
    headers = {'content_Type': 'application/json'}
    print('requesturl:', url)
    response = requests.put(url, json=body, headers=headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


def deletedata(url, opheader=None):
    headers = {'content-Type': 'application/json'}
    headers = (headers | opheader) if isinstance(opheader, dict) else headers
    response = requests.delete(url, verify=False, headers=headers)
    print(response, requests, headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken
