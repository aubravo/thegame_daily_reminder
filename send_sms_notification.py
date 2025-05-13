import random
import logging

from twilio.rest import Client

from settings import Settings

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

settings = Settings()
if not settings.twilio_account_id and not settings.twilio_auth_token: 
    raise Exception("Missing Twilio account settings")
client = Client(settings.twilio_account_id, settings.twilio_auth_token)

def get_message_list():
    if settings.thegame_message_file and not settings.thegame_use_sample:
        with open(settings.thegame_message_file) as message_file:
            return [line.rstrip() for line in message_file]
    if settings.thegame_use_sample:
        with open(f'./message_samples_{settings.thegame_sample_language}.txt') as message_file:
            return [line.rstrip() for line in message_file]
    logger.warning("No sample used or message file found.")
    return []

message_list = get_message_list()
message = message_list[random.randint(0,len(message_list))]
with open(settings.thegame_phone_list) as phone_list_file:
    phone_list = [line.rstrip() for line in phone_list_file]
for phone in phone_list:
    print(f"Sending message {message} to {phone}")
    twilio_message = client.messages.create(
            body=message,
            from_=settings.twilio_from_phone,
            to=phone,
            )
    logger.info(msg=f"{twilio_message.status}")

