# setup flask
import requests
from flask import Flask, request

app = Flask(__name__)


class Webhook_obj:
    '''store webhook'''

    def __init__(self) -> None:
        self.saved_webhook = ''


webhook = Webhook_obj()
# '/'->(post) endpoint to receive webhook from wa


@app.route('/', methods=['POST', 'GET'])
def getMessage():
    update = request
    # Dispatcher.process_update(update)
    requests.post(get_webhook(), data=update)
    return "running", 200

# '/create-webhook'-> (post) endpoint to receive webhook
# '/delete-webhook'->(post) endpoint to delete current webhook


def delete_webhook():
    pass


def create_webhook(url):
    delete_webhook()
    # create


def get_webhook() -> str:
    # fetch saved webhook
    res = webhook.saved_webhook  # fetched hook
    return res

# for "/":


def forward_webhook():
    wbhk = get_webhook()
    # requests.post(wbhk,data=response
    return 200  # status


# In client
# On app run:
# ___update webhook
#   requests.post(forwarder_url/create_webhook, data=(new_webhook))
