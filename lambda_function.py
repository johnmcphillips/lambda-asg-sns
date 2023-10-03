import boto3
import json
import urllib3
import ast
import logging
from base64 import b64decode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

http = urllib3.PoolManager()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    url = "https://hooks.slack.com/services/xxxxxx"
    headers = {
        "Content-Type": "application/json"
    }

    try:
        message = event['Records'][0]['Sns']['Message']
        # Check if the message is a string containing 'null' and convert it to None
        if message.strip().lower() == 'null':
            message = None
        else:
            message = json.loads(message)  # Assuming the message is valid JSON

        if message is not None:
            reason = message['Cause']
            msg = json.dumps({
                "channel": "#channel",
                "username": "username",
                "text": reason,
                "icon_emoji": ":ghost:"
            })
            http.request('POST', url=url, body=msg, headers=headers)
            #print(reason)
        else:
            logger.warning("Received 'null' message, ignoring.")
        
        logger.info("Event: " + str(event))
    
    except KeyError as e:
        logger.error(f"KeyError: {str(e)}")
    except json.JSONDecodeError as e:
        logger.error(f"JSONDecodeError: {str(e)}")
