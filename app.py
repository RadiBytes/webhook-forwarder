from src.webhook import webhook
from src.config import DEBUG, SUBPATH

#--------- Optional Settings ------#
# Add subdirectory for your webhook URL. Default is empty string
webhook.add_subpath = SUBPATH

# Set debug mode. Default is True
webhook.debug = DEBUG

# set to "hub.challenge" for whatsapp api webhooksetup
# otherwise, leave empty. Default is empty
webhook.verify_query_key = "hub.challenge"

#--------- End Optional Settings ------#
webhook.run()
