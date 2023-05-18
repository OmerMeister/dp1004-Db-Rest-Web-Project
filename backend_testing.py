import json
import requests
from db_connector import db_get
import time


# the test makes a post request the rest api. then, checks the result for the request id with the get api and the db
# if all the results are corresponding, the test success
# the method gets an id (int) and a username (string)
def backend_testing(id, username):
    # using post to create a user
    rest_returned_username = -1
    db_returned_username = -1
    user_obj = '{"user_name": "%s"} ' % username
    try:
        post_request = requests.post(f'http://127.0.0.1:5000/users/{id}', json=json.loads(user_obj))
        time.sleep(0.5)
        print(f"post response: {post_request.text}")  # for debugging
    except Exception as e:
        print("post error occurred: ", e)
    # making get request to make sure
    try:
        response = requests.get(f'http://127.0.0.1:5000/users/{id}')
        rest_returned_username = response.json()['user_name']
    except Exception as e:
        print("get error occurred: ", e)
    # making db request to make sure
    try:
        db_returned_username = db_get(id)
    except Exception as e:
        print("db error occurred: ", e)
    # comparing all three variables
    if (rest_returned_username == username and db_returned_username == username):
        print("post and get succeeded. username is:", username)
    else:
        print("backend test failed")


backend_testing(33, "bacardi rum")
