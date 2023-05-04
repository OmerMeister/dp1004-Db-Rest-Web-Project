from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

'''
for edge:
from selenium.webdriver.edge.service import Service
service = Service('C:/Users/Omer/PycharmProjects/msedgedriver.exe')
driver = webdriver.Edge(service=service)
'''
# for chrome:
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("C:/Users/Omer/PycharmProjects/chromedriver.exe"))


def frontend_test(id):
    print("starting test with id: ", id)
    driver.get(f'http://127.0.0.1:5001/get_user_name/{id}')
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "div")))
    print("page finished loading")
    try:
        element = driver.find_element(By.ID, "user")
        print(f"user found!  the username is " + element.text)
        sleep(10)
    except Exception as e:
        print("user did not found, error:", e)
    finally:
        driver.quit()


frontend_test(11)

'''
find_element(By.CLASS_NAME, "er8xn")
element.send_keys("תביא לי")
element.send_keys(Keys.ENTER)
element.send_keys(Keys.ENTER)
'''
