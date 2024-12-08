"""setup flask"""

import os
import requests
from flask import Flask, request
from waitress import serve


IS_WHATSAPP = True


app = Flask(__name__)


class _Webhook_obj:
    '''Initialize webhook settings'''

    def __init__(self) -> None:
        self.webhook_forward_url: str = ""
        self._subpath: str = ''
        # set to "hub.challenge" for whatsapp api webhooksetup
        self.verify_query_key: str = "hub.challenge" if IS_WHATSAPP else ''
        self.debug = True

    def add_subpath(self, text: str):
        self._subpath = text.strip('/')

    def run(self):
        if self.debug:
            print(
                f"""***** Running Webhook Forwarder *****
        Receivning at: /{self._subpath}
        Forwarding to: {self.webhook_forward_url}"""
            )
            app.run(debug=self.debug, host="0.0.0.0", port=os.getenv("PORT"))
        else:
            print(
                f"""***** Running Webhook Forwarder *****
        Receivning at: /{self._subpath}
        Forwarding to: {self.webhook_forward_url}"""
            )
        serve(app, host='0.0.0.0', port=os.getenv(
            "PORT") if os.getenv("PORT") else 80)


webhook = _Webhook_obj()
# '/'->(post) endpoint to receive webhook from wa


@app.route('/'+webhook._subpath, methods=['POST', 'GET'])
def forward_message():
    # send response to saved webhook
    if request.method == "POST":
        update = request.data.decode('utf-8')  # .get_json(force=True)
        args = update
        print("Received:\n", request.json)
        try:
            print("sent to", webhook.webhook_forward_url)
            return requests.post(webhook.webhook_forward_url, data=update).text
        except:
            print("Forward not successful")
    else:
        try:
            args = request.args.to_dict()
            args = args[webhook.verify_query_key]
        except KeyError:
            args = "Running, no args"
        print("challenge is: ", args)
    return args, 200


@app.route('/webhook', methods=['POST', 'GET'])
def forward_webhook():
    # send response to saved webhook
    if request.method == "POST":
        riddle = request.headers.get('riddle')
        print("riddle is",riddle)
        if not "xypprice__pally2o22__"==riddle:
            print('failed riddle',riddle)
            return f"failed riddle {riddle}", 400
        update = request.data.decode('utf-8')  # .get_json(force=True)
        args = update
        # update = json.loads(update)

        try:
            requests.post(webhook.webhook_forward_url + "/webhook", data=update).text
            print("sent to", webhook.webhook_forward_url)
            return f"success: forwarded", 200
        except:
            print("Forward not successful")
            return f"success: Forward not successful ", 200
    else:
        try:
            args = request.args.to_dict()
            args = args[webhook.verify_query_key]
            print("challenge is: ",args)
        except KeyError:
            args = "webhook get nothing here"
    return args, 200


@app.route('/delete_webhook')
def delete_webhook():
    webhook.webhook_forward_url = ""
    return "success", 200


@app.route('/setwebhook', methods=['POST', 'GET'])
def set_webhook():
    if request.method == "POST":
        update = request.get_json(force=True)
        try:
            webhook_forward_url = update["webhook_url"]
            webhook.webhook_forward_url = webhook_forward_url
            print(f"set webhook success to {webhook.webhook_forward_url}")
            return f"set webhook success to {webhook.webhook_forward_url}", 200
        except:
            print("Could not set webhook_forward_url")
            return "Could not set webhook_forward_url", 402
    return f"webhook url is {webhook.webhook_forward_url}", 200


if __name__ == "__main__":
    if webhook.debug:
        print(
            f"""***** Running Webhook Forwarder *****
        Receivning at: /{webhook._subpath}
        Forwarding to: {webhook.webhook_forward_url}"""
        )
        app.run(debug=webhook.debug, host="0.0.0.0", port=os.getenv("PORT"))
    else:
        print(
            f"""***** Running Webhook Forwarder *****
        Receivning at: /{webhook._subpath}
        Forwarding to: {webhook.webhook_forward_url}"""
        )
        serve(app, host='0.0.0.0', port=os.getenv(
            "PORT") if os.getenv("PORT") else 80)
