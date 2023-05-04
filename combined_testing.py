import json
import time
import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By

# Establishing a connection to DB
schema_name = "sql7615064"
conn = pymysql.connect(host='sql7.freemysqlhosting.net', port=3306, user='sql7615064', passwd='rRsh6tSbEB',
                       db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# for chrome:
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("C:/Users/Omer/PycharmProjects/chromedriver.exe"))


# gets an id (int) and username (string) and make a post request. then, checks with get request that the new user
# exists, then directly query the db for the newly created user.
def combined_testing(id, username):
    backendtest_bool = False
    dbtest_bool = False
    frontendtest_bool = False
    # sections 1,2
    user_obj = {"user_name": username}
    try:
        requests.post(f'http://127.0.0.1:5000/users/{id}', json=json.dumps(user_obj)) #post request
        time.sleep(0.5)
        response = requests.get(f'http://127.0.0.1:5000/users/{id}')
        rest_returned_username = json.loads(response.text).get('user_name')
        if (rest_returned_username == username):
            backendtest_bool = True
    except Exception as e:
        print("backend test failed with this error: ", e)
        raise Exception("backend test failed")
    # section 3
    try:
        cursor.execute(f"SELECT * FROM users where user_id='{id}';")
        db_user_name = cursor.fetchone()[1]  # fetchone returns a tuple
        if (db_user_name == username):
            dbtest_bool = True
    except Exception as e:
        print("db test failed with this error: ", e)  # for debugging
        raise Exception("db test failed")
    # section 4,5,6
    try:
        driver.get(f'http://127.0.0.1:5001/get_user_name/{id}')
        element = driver.find_element(By.ID, "user")
        if (element.text == username):
            frontendtest_bool = True
            driver.quit()
    except Exception as e:
        print("frontend test failed with this error: ")  # for debugging
        raise Exception("frontend test failed")
        driver.quit()

    if (backendtest_bool and dbtest_bool and frontendtest_bool):
        print("all tests passed!")


combined_testing(51, "mike pearson")
