# A webhook forwarding client based on Python

Simple webhook forwarder script to send webhooks from a hosted url to your local machine that has a tunneling service such as Ngrok set up.

## Example usecase

Many services such as Whatsapp Business Cloud only send out updates via webhook. To receive these updates, you have to register a webhook url beforehand. During development, you would typically use a service like Ngrok to tunnel the webhook requests to your local machine. The issue with this is that for the free version of Ngrok, a new url is generated everytime you restart the service, and then you would have to manually.
A good solution is to host this forwarding client on a virtual server (e.g Heroku) and using its url as your webhook address, then sending a simple post request to the endpoint 'https://herokuapp.your-app-name.app/setwebhook' with the new ngrok url (I have a script to get this url too)

## How to use

To use for Whatsapp Business Cloud Api (which is what prompted my to write this script):

1. Deploy this app to heroku as is. If you're not deploying to heroku, then the process might be different.
   For extra customization such as using a subpath, navigate to src/config.py and edit the SUBPATH variable to the subpath you want to receive your webhooks in.

2. Use the app's url as your webhook url. e.g https://herokuapp.your-app-name.app

3. Clone this repo to your project directory.

## For Python

4. pip install requests
5. To update the heroku app with your ngrok url, you need to import the update_webhook function from the cloned directory. e.g from .webhook-forwarder.client import update_webhook
6. Call the update_webhook function passing in the url of the deployed heroku app only. Ensure that ngrok is already running at this point.

## For Node

4. npm install axios
5. To update the heroku app with your ngrok url, you need to import the update_webhook function from the cloned directory. e.g import update_webhook from ./webhook-forwarder/client or const update_webhook = require("./webhook-forwarder/client")
6. Call the update_webhook function passing in the url of the deployed heroku app only. Ensure that ngrok is already running at this point.
