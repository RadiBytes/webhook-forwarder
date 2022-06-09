# setup flask
import requests
from flask import Flask, request

app = Flask(__name__)


class _Webhook_obj:
    '''store webhook'''

    def __init__(self) -> None:
        self.saved_webhook = ''
        self.subdir = ""

    def add_subdir(self, text: str):
        self.subdir = text.strip('/')

    def set_new_webhook(self, text: str):
        self.saved_webhook = text


webhook = _Webhook_obj()
# '/'->(post) endpoint to receive webhook from wa


@app.route('/'+webhook.subdir, methods=['POST', 'GET'])
def forward_message():
    update = request
    # send response to saved webhook
    requests.post(webhook.saved_webhook, data=update)
    return "running", 200


@app.route('/delete_webhook')
def delete_webhook():
    webhook.set_new_webhook("")


@app.route('/set_webhook', methods=['POST', 'GET'])
def set_webhook():
    update = request.get_json(force=True)
    try:
        webhook_url = update[""]
        webhook.set_new_webhook(webhook_url)
    except:
        return "Could not set webhook_url", 402


# In client
# On app run:
# ___update webhook
#   requests.post(forwarder_url/create_webhook, data=(new_webhook))
