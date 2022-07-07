from src.webhook import webhook
from src.config import DEBUG

#--------- Optional Settings ------#
# Add subdirectory for your webhook URL. Default is empty string
webhook.add_subdir = ""

# set to "hub.challenge" for whatsapp api webhooksetup
# otherwise, leave empty. Default is empty
webhook.verify_query_key = "hub.challenge"

#--------- End Optional Settings ------#
webhook.run()
