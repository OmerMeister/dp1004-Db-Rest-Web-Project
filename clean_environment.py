import requests
from requests import ConnectTimeout

print("trying to stop web_app and rest_app\n")

try:
    requests.get('http://127.0.0.1:5000/stop_server',timeout=7)
    print("rest app stopped\n")
except ConnectTimeout:
    print('Request has timed out (7 sec) on terminating "rest_app"')
except Exception as e:
    print('unknown exception occurred on terminating "rest_app". exceptions is:')
    print(e)
    print("")

try:
    requests.get('http://127.0.0.1:5001/stop_server')
    print("web app stopped")
except ConnectTimeout:
    print('Request has timed out (7 sec) on terminating "web_app"')
except Exception as e:
    print('unknown exception occurred on terminating "web_app". exceptions is:')
    print(e)

