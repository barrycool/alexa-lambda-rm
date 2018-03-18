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

powerCtrl = {
    "directive": {
        "endpoint": {
            "cookie": {
                "detail1": "For simplicity, this is the only appliance",
                "detail2": "that has some values in the additionalApplianceDetails"
            },
            "endpointId": "switch-001",
            "scope": {
                "token": "b1e0fb5235f6a046054edcd029f2d6b54223d279",
                "type": "BearerToken"
            }
        },
        "header": {
            "correlationToken": "AAAAAAAAAAAtViy2g+9AWECtWdTIKQ43BAIAAAAAAADpU4lb3+LleYXaxuh5yw5dwNSl9efiDe8pND32B6UF4+/zY9ltqU14kAxW8nQ/WHjZdEvUSND0YPWR8vKrqidHxFaxZVqiWJTuqdYajzL+vYwnT7hnP7HRJXnnl75LEPB0I0tqdh6xmOcj49bBCI7q6ayS9QinYhybtPxjGldCqnPvgb6ktpMPS+uzts8rRX0bF/W/DiwgEzSXLas2mHnCpamD8VpytcxPWy3As2FBJ2ges+ELwQDvSEV+/njEkBMuCQNvA1DEFdifM/ZLxkEEy+0HSxUXS8az2mZbwlwg/zEMKmMq4M/Te1zURKT6ZyptLFly24w5lsHwXlX8jFhrgu7nPKNPUNCiuLbsMgbbCIwsUebi1Qk14aTOIjOWswFZ4rGBigkW7Njr8nPy9FJQgFGJyR1hpWJPnYtffJ5LzNTMo8wHgrByyRUJx0YSZ6K3trm5u4+L2xXK74LfjQiGqXPcn0IX0nqOWkNwMl0/oDgB/kGA5JrrYrCiviz/jd7S+88OMkfd0H5fv584zgydQqav0rVKT+p4u493jHyn7hhYwvbfikb9Yb5ngcXVR29taxTSp7Nh93d4A8EafUVTEzL8iNsPOSkYkzMjl9jdONIDVSrfYOHntqhOts726sDV7nCShhBApJ1m7p0W8Z9Nweb3Rg6DcTD6SJawQaUAo+SlEn4=",
            "messageId": "d720369d-38e4-44d7-a6a8-c4d004ad3feb",
            "name": "ReportState",
            "namespace": "Alexa",
            "payloadVersion": "3"
        },
        "payload": {}
    }
}
request = powerCtrl
context = ''

lambda_handler(request, context)

