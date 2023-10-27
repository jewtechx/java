import requests
import cowsay

def fetchApi(api):
    apidata = requests.get(api)
    if apidata.status_code == 200:
        apijson = apidata.json()
    return apijson

def letCowSay(words):
    cowsaid = cowsay.cow(words)
    return cowsaid


