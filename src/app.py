# setup flask
import os
import requests
from flask import Flask, request
from waitress import serve
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


class _Webhook_obj:
    '''Initialize webhook settings'''

    def __init__(self) -> None:
        self.webhook_url = ''
        self.subdir = ""
        self.debug = True
        self.port = 80

    def add_subdir(self, text: str):
        self.subdir = text.strip('/')

    def run(self):
        if self.debug:
            print(f"""***** Running Webhook Forwarder *****
        Receivning at: /{self.subdir}
        Forwarding to: {self.webhook_url}""")
            app.run(debug=self.debug, host="0.0.0.0")
        else:
            print(f"""***** Running Webhook Forwarder *****
        Receivning at: /{self.subdir}
        Forwarding to: {self.webhook_url}""")
        serve(app, host='0.0.0.0', port=int(self.port) if self.port else 80)


webhook = _Webhook_obj()
# '/'->(post) endpoint to receive webhook from wa


@app.route('/'+webhook.subdir, methods=['POST', 'GET'])
def forward_message():
    # send response to saved webhook
    if request.method == "POST":
        update = request.get_json(force=True)
        # Dispatcher.process_update(update)
        # delete()
        args = update
    try:
        args = request.args.to_dict()
        args = args["hub.challenge"]  # Used for whatsapp api webhooksetup
    except KeyError:
        args = "Running, no args"
    return args, 200


@app.route('/delete_webhook')
def delete_webhook():
    webhook.webhook_url = ""
    return "success", 200


@app.route('/setwebhook', methods=['POST', 'GET'])
def set_webhook():
    if request.method == "POST":
        update = request.get_json(force=True)
        try:
            _webhook_url = update["webhook_url"]
            webhook.webhook_url = _webhook_url
            return "set webhook success", 200
        except:
            return "Could not set webhook_url", 402
    return "set webhook url", 200


webhook.webhook_url = "ra"

if __name__ == "__main__":
    print(f"""***************** Running Webhook Forwarder *****************
    Receivning at: /{webhook.subdir}
    Forwarding to: {webhook.webhook_url}""")
    app.run(debug=webhook.debug, host="0.0.0.0", port=os.getenv("PORT"))
