# A webhook forwarding client based on Python

## Example usecase

You need to process webhook requests on local server and you're using a port exposing service like Ngrok which changes address everytime you restart., and you don't want to always manually login and update the webhook address in the sending app.
A good solution would be to host this forwarding client on a virtual server (e.g Heroku) to get a permanent address and then supplying the server address to your webhook sender.

Then in your local dev server...
