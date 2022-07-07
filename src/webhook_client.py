import requests
import json


ngrok_data = requests.get("http://localhost:4040/api/tunnels").json()
try:
    ngrok_url = ngrok_data["tunnels"][0]["public_url"]
except:
    ngrok_url = None


def update_webhook(server_url, subpath=''):
    """Use this on target machine(client) to send the current url where all webhhooks should be forwarded to
    Args:
        server_url:str= The base address of where the webhook forwarder is hosted (the permanent url of the hosted server
                        i.e: https://herokuapp.xyzapp.app)"""
    payload = {"webhook_url": ngrok_url+'/'+subpath.strip('/')}
    _url = f"{server_url.strip('/')}/setwebhook"
    return requests.post(url=_url, data=json.dumps(payload)).text
