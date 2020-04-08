import requests
import json
import cv2
import numpy as np
import base64

url = 'http://127.0.0.1:5000/api/Hello'

headers = {
        'authorization': "Basic ZXNlbnRpcmVcYdddddddddddddd",
        'cache-control': "no-cache",
    }

data = open('./dog.jpg', 'rb').read()
print("Request Sent")

response = requests.request("POST", verify=False, url=url, data=data, headers=headers)

print(response)
print("Request successful")
