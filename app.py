from src.webhook import webhook

#--------- Optional Settings ------#
# Add subdirectory for your webhook URL. Default is empty string
webhook.add_subdir = ""

# Set debug mode. Default is True
webhook.debug = False

# set to "hub.challenge" for whatsapp api webhooksetup
# otherwise, leave empty. Default is empty
webhook.verify_query_key = "hub.challenge"

#--------- End Optional Settings ------#
webhook.run()
