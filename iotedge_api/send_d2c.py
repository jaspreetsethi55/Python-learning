import requests

def set_request_params():
    request_json = {
      "data": [
        {
            "message": { 'a' :  '\1\c\45c' }
       #   "deviceId": "test-d2c"
        }
      ],
      "responseCallback": "https://webhook.site/9cdf068c-2642-467a-aaff-8876c3a4dcf9"
    }

    headers = {'Content-type': 'application/json', 'x-correlation-id': '12345', 'Accept': 'application/json'}
    return request_json,headers

url = 'http://10.98.0.167:80/api/v1/devices/messages'
def send_d2c_request():
    request_json,headers = set_request_params()
    r = requests.post(url, json=request_json, headers=headers)
    return r

r = send_d2c_request()
print(r.text)
