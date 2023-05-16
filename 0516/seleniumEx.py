# selenium.py

import time 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

'''driver.get("https://travel.naver.com/overseas")
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/a[3]").click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[3]/div/div/div[2]/a[2]").click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[3]/div/div/div[4]/div/div[1]/a[4]").click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[3]/div/div/div[4]/div/div[2]/div[4]/a").click #send_keys("일본")
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[3]/div/div/div[4]/div/div[2]/div[4]/div/a[1]").click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[3]/div/div/div[4]/ul/li[3]/a").click()
time.sleep(5)

driver.find_element(By.XPATH, "").click()
time.sleep(5)

driver.find_element(By.XPATH, "").click()
time.sleep(5)

#time.sleep(2)
#newsTitle = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/h2").text'''


driver.get("https://finance.naver.com/")
time.sleep(5)

subject = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/a").text
print(subject)
subject = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/a").text
print(subject)
subject = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/a").text
print(subject)
subject = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[4]/a").text
print(subject)

list1 = []
for i in range(10):
    subject = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[i+1]/a").text
    list1.append(subject)

print(list1)
