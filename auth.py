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

powerCtrl = \
{ \
    "directive": { \
        "header": { \
            "messageId": "2d01986e-51d8-4d99-a952-2dfb2b847a23", \
            "name": "AcceptGrant", \
            "namespace": "Alexa.Authorization", \
            "payloadVersion": "3" \
        }, \
        "payload": { \
            "grant": { \
                "code": "ANjCqmmdjQewJOtATCKH", \
                "type": "OAuth2.AuthorizationCode" \
            }, \
            "grantee": { \
                "token": "81bd823523a5848022aeea1d85a6c5f57d75cc8e", \
                "type": "BearerToken" \
            } \
        } \
    } \
} \

request = powerCtrl
context = ''

lambda_handler(request, context)

