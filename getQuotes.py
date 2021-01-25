import json
import os
import sys
import logging
import requests
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add vendor directory to module search path
parent_dir = os.path.abspath(os.path.dirname(__file__))
libraries_dir = os.path.join(parent_dir, 'libraries')
sys.path.append(libraries_dir)

API_KEY = "<<<ADD API KEY HERE>>>"
function = "GLOBAL_QUOTE"

def main(event, context):
    code = event["queryStringParameters"]["code"]
    #for value in event.keys():
     #   logger.info(value)
    
    quote = requests.get('https://www.alphavantage.co/query?function='+function+'&symbol='+code+'.SA&apikey='+API_KEY).json()["Global Quote"]
    print("'Current quote' request received for code:" + code)
    # https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=PETR4.SA&apikey=
    

    body = ""
    status = 404

    if(quote):
        body = quote["05. price"]
        status = 200
    return {
        "isBase64Encoded": "false",
        "statusCode": status,
        "headers": { "headerName": "headerValue"},
        "multiValueHeaders": { "headerName": ["headerValue", "headerValue2"]},
        "body": body
    }

#main({"queryStringParameters" : {"code" : "PETR4"}}, "")