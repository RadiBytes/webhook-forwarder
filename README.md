# A webhook forwarding client based on Python

Simple webhook forwarder script to send webhooks from a hosted url to your local machine without that has a tunneling service such as Ngrok set up.

## Example usecase

Processing webhook requests from a service such as Discord or Meta on local server and you're using a tunneling service like Ngrok. But the generated ngrok address changes everytime you restart the tunnel for the free tier. So, you don't want to always manually login and update the webhook address (as is the case with Discord and Meta).
A good solution is to host this forwarding client on a virtual server (e.g Heroku) and using its url as your webhook address for Meta.

## How to use
