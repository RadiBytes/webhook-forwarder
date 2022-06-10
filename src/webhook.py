# setup flask
import os
import json
import requests
from flask import Flask, request
from waitress import serve


app = Flask(__name__)


class _Webhook_obj:
    '''Initialize webhook settings'''

    def __init__(self) -> None:
        self._webhook_forward_url: str = ''
        self._subdir: str = ""
        # set to "hub.challenge" for whatsapp api webhooksetup
        self.verify_query_key: str = ""
        self.debug = True

    def add_subdir(self, text: str):
        self._subdir = text.strip('/')

    def run(self):
        if self.debug:
            print(f"""***** Running Webhook Forwarder *****
        Receivning at: /{self._subdir}
        Forwarding to: {self._webhook_forward_url}""")
            app.run(debug=self.debug, host="0.0.0.0", port=os.getenv("PORT"))
        else:
            print(f"""***** Running Webhook Forwarder *****
        Receivning at: /{self._subdir}
        Forwarding to: {self._webhook_forward_url}""")
        serve(app, host='0.0.0.0', port=os.getenv(
            "PORT") if os.getenv("PORT") else 80)


webhook = _Webhook_obj()
# '/'->(post) endpoint to receive webhook from wa


@app.route('/'+webhook._subdir, methods=['POST', 'GET'])
def forward_message():
    # send response to saved webhook
    if request.method == "POST":
        update = request  # .get_json(force=True)
        args = update
        try:
            requests.post(webhook._webhook_forward_url, data=update)
            print("sent to", webhook._webhook_forward_url)
        except:
            print("Forward not successful")
    else:
        try:
            args = request.args.to_dict()
            args = args[str(webhook.verify_query_key)]
        except KeyError:
            args = "Running, no args"
    return args, 200


@app.route('/delete_webhook')
def delete_webhook():
    webhook._webhook_forward_url = ""
    return "success", 200


@app.route('/setwebhook', methods=['POST', 'GET'])
def set_webhook():
    if request.method == "POST":
        update = request.get_json(force=True)
        try:
            _webhook_forward_url = update["webhook_url"]
            webhook._webhook_forward_url = _webhook_forward_url
            return "set webhook success", 200
        except:
            return "Could not set _webhook_forward_url", 402
    return "set webhook url", 200


if __name__ == "__main__":
    if webhook.debug:
        print(f"""***** Running Webhook Forwarder *****
        Receivning at: /{webhook._subdir}
        Forwarding to: {webhook._webhook_forward_url}""")
        app.run(debug=webhook.debug, host="0.0.0.0", port=os.getenv("PORT"))
    else:
        print(f"""***** Running Webhook Forwarder *****
        Receivning at: /{webhook._subdir}
        Forwarding to: {webhook._webhook_forward_url}""")
        serve(app, host='0.0.0.0', port=os.getenv(
            "PORT") if os.getenv("PORT") else 80)