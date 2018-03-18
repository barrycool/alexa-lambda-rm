#!/usr/bin/python3

import logging
import json
from lambda_function import lambda_handler

# Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
st = logging.StreamHandler()
st.setLevel(logging.INFO)
logger.addHandler(st)

discover= \
{ \
    "directive": { \
        "header": { \
            "namespace": "Alexa.Discovery", \
            "name": "Discover", \
            "payloadVersion": "3", \
            "messageId": "1bd5d003-31b9-476f-ad03-71d471922820" \
        }, \
        "payload": { \
            "scope": { \
                "type": "BearerToken", \
                "token": "access-token-from-skill" \
            } \
        } \
    } \
} \

request = discover
context = ''

lambda_handler(request, context)

