#!/usr/bin/python3

import json
from lambda_function import lambda_handler

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

