from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service("C:/Users/Omer/PycharmProjects/chromedriver.exe"))


def frontend_test(id):
    print("starting test with id: ", id)
    #driver.get(f'http://127.0.0.1:5001/get_user_name/{id}')
    driver.get(f'http://ynet.co.il')
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "div")))
    print("page finished loading")
    try:
        element = driver.find_element(By.ID, "user")
        print(f"user found!  the username is "+element.text)
    except:
        print("user did not found")
    sleep(10)
    driver.quit()


frontend_test(18)

'''
find_element(By.CLASS_NAME, "er8xn")
element.send_keys("תביא לי")
element.send_keys(Keys.ENTER)
element.send_keys(Keys.ENTER)
'''
