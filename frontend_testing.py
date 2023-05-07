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


# function gets an id (int) and checks if the rendered html on the browser has a "user" tag (shows only if user exists)
# prints the result to the console
def frontend_test(id):
    print("starting test with id: ", id)
    driver.get(f'http://127.0.0.1:5001/get_user_name/{id}')
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "div")))
    print("page finished loading")
    try:
        element = driver.find_element(By.ID, "user")
        print(f"user found!  the username is " + element.text)
        sleep(5)
    except:
        sleep(2)
        print("user did not found")
    finally:
        driver.quit()


frontend_test(53)
