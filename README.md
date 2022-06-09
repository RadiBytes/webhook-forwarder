# A webhook forwarding client based on Python

## Example usecase

You need to process webhook requests on local server and you're using a tunneling service like Ngrok. But the generated address changes everytime you restart the service. So, you don't want to always manually login and update the webhook address (as is the case with Discord and Meta).
A good solution is to host this forwarding client on a virtual server (e.g Heroku) to get a permanent address and then supplying the server address to your webhook sender.

Then in your local dev server, use this example code to setup...
