from wox import Wox, WoxAPI
import webbrowser
import urllib.parse
import requests
import wolframalpha
from appid import APP_ID


DEFAULT_RESULT = {
    'Title': 'Open wolframalpha.com in browser',
    'SubTitle': '',
    'IcoPath': 'wolframURL.png',
    'JsonRPCAction': {
        'method': 'openUrl',
        'parameters': ['https://www.wolframalpha.com/']
    }
}

APPID_RESULT = {
    'Title': 'Sign up for a Wolfram Alpha AppId',
    'SubTitle': '',
    'IcoPath': 'wolframURL.png',
    'JsonRPCAction': {
        'method': 'openUrl',
        'parameters': ['https://products.wolframalpha.com/api/']
    }
}

client = wolframalpha.Client(APP_ID)
api_url = 'http://api.wolframalpha.com/v1/result?appid={}&units=metric&i='.format(APP_ID)

class Wolfram(Wox):

    def copy(self, text):
        # clipboard.copy(text)
        return text

    def openUrl(self, url):
        webbrowser.open(url)

    def query(self,key):
        results = []
        if key.strip() == '':
            results.append(DEFAULT_RESULT)
            results.append(APPID_RESULT)
        else:
            keyurl = urllib.parse.quote_plus(key)
            urlquery = api_url + str(keyurl)
            res = requests.get(urlquery)
            results.append({
                "SubTitle": key,
                "Title": res.text,
                "IcoPath":"wolfram.png",
                "ContextData": key,
                "JsonRPCAction":{
                    "method": "openUrl",
                    "parameters": [f"https://www.wolframalpha.com/input?i={keyurl}"]
                }
            })
        return results

    def context_menu(self, data):
        results = []
        keyurl = urllib.parse.quote_plus(data)
        urlquery = 'https://www.wolframalpha.com/input/?i=' + str(keyurl)
        res = client.query(data)
        for pod in res.pods:
            title = pod.title
            for sub in pod.subpods:
                if sub["plaintext"]:
                    results.append({
                        "SubTitle": sub["plaintext"],
                        "Title": title,
                        "IcoPath":"wolfram.png",
                        "JsonRPCAction":{
                            "method": "copy",
                            "parameters": [sub["plaintext"]]
                        }
                    })
        results.append({
            "Title": "Open result in browser",
            "SubTitle": "",
            "IcoPath": "wolframURL.png",
            "JsonRPCAction":{
                "method": "openUrl",
                "parameters": [urlquery]
            }
        })
        return results

if __name__ == "__main__":
    Wolfram()