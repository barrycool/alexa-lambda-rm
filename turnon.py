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
    "endpoint": { \
      "cookie": { \
        "detail1": "For simplicity, this is the only appliance", \
        "detail2": "that has some values in the additionalApplianceDetails" \
      }, \
      "endpointId": "2c3ae810eddd", \
      "scope": { \
        "token": "7b59bdad4683b25123d052d4fde2b2930a56c536", \
        "type": "BearerToken" \
      } \
    }, \
    "header": { \
      "correlationToken": "AAAAAAAAAAB44WyFvEZdwZV+76MZzkRcBAIAAAAAAABfWePHuRLDorWjAUPsVVjbQcXNdPyO6xMFdr8bAkBhik38zdINI+GaxFxr0Nrb2cyrCs2ZD2iOX4SXV072coelnyaraqOvFyFKonn6pf0NSZM7NknBFedn+ALbtXTMjAuRfh7gfVj1zS7ZT6HqaT57TiiCviIvrnebt3yRw41jts68xOjK1pPB44j++GZC9VXiUF2QiN/0KXmAo2ogjK216CGMcBhqEOtKGNOtHBYp0hGEn97k09Ctx6L+RH5BRPic99QBWHPyRdoOaj1KFV1ENNzUGvFNJhDEH+XVbpLDkoOhLRAF3J1Plwmr4FXIChG6KgB5sRsoqyNzO25RqNsRc2ndgR+W7UOJoCxooIbGvYG3biPbY0PG+P3fXd4zj2aiGFvRE66fdY9Tqi1k+J1IwCW0Ku78isXRmPM1w59HtXYbZo3DIQ2anPb7/KbgPWKZ2dJCIYpD35Zsy9hNlxo7m2Y7xa/1Xu8BdOaGh7tib5/JjalNtbcAYlq1KD7QLHEzS78pIhIZrqnvbp6Sl07/bcoQFYEzD0/uivt7e/PghU5ebMEJFLQ1r7Q8aRqMQAcsLMs1NfK2utXcwyKRS3/NvmuCyNTpGR8cUsoaX4XG/5YTEBvk+ptZuxzNprLcEkmIQdodx3FMODukCJ2WkbJOZYBzJHEtDHxJbE7NgNu75ud3UhE=", \
      "messageId": "c4b6a5bc-f81e-4378-840b-c78821d2d475", \
      "name": "TurnOn", \
      "namespace": "Alexa.PowerController", \
      "payloadVersion": "3" \
    }, \
    "payload": {} \
  } \
} \

request = powerCtrl
context = ''

lambda_handler(request, context)

