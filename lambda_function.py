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
    url = "https://hooks.slack.com/services/xxxx/xxxx/xxxx"
    headers = {
        "Content-Type": "application/json"
    }
    
    message = event['Records'][0]['Sns']['Message']
    logger.info("Event: " + str(event))
    logger.info("Message: " + str(message))
    
    message = ast.literal_eval(event['Records'][0]['Sns']['Message'])
    reason = message['Cause']
    
    msg = json.dumps({
        "channel": "#your-channel",
        "username": "username",
        "text": reason,
        "icon_emoji": ":ghost:"
    })
    http.request('POST',url=url, body=msg, headers=headers)
    
    


