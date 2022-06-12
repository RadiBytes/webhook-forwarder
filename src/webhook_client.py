import requests
import json


def update_webhook(server_url, webhook_url):
    """Use this on target machine(client) to send the current url where all webhhooks should be forwarded to
    Args:
        server_url:str= The base address of where the webhook forwarder is hosted (the permanent url of the hosted server
                        i.e: https://herokuapp.xyzapp.app)
        webhook_url:str= The url where all webhooks should be forwarded to  """
    payload = {"webhook_url": webhook_url}
    _url = f"{server_url.strip('/')}/setwebhook"
    return requests.post(url=_url, data=json.dumps(payload))
