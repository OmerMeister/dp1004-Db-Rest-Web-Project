import json
import requests
from db_connector import db_get
import time

def backend_testing(id, username):
    # using post to create a user
    user_obj = {"user_name": username}
    try:
        post_request = requests.post(f'http://127.0.0.1:5000/users/{id}', json=json.dumps(user_obj))
        time.sleep(0.5)
        print(f"Response: {post_request.text}")  # for debugging
    except Exception as e:
        print("post error occurred: ", e)
    # making get request to make sure
    try:
        response = requests.get(f'http://127.0.0.1:5000/users/{id}')
        rest_returned_username = json.loads(response.text).get('user_name')
        db_returned_username = db_get(id)
        if (rest_returned_username == username and db_returned_username == username):
            print("post and get succeeded. username is: ", username)
    except Exception as e:
        print("get error occurred: ", e)


backend_testing(24, "boaz golan")
