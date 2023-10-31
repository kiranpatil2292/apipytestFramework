import requests, json


def getapiData(url):
    headers = {"content-Type": "application/json"}
    response = requests.get(url, verify=False)
    return response


def postapiData(url,payload,headers):

    response = requests.get(url, verify=False)
    return response
