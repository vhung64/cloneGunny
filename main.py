from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
import json
import base64
import requests
import sys

while True:
    def getImage():
        time.sleep(1)
        image = driver.find_element(By.XPATH, value='/html/body/app-root/div[1]/div[2]/div/div/div[2]/div[2]/app-account/app-menu/article/div/div[2]/div/div[2]/form/div[7]/div/span[1]/img')
        image_url = image.get_attribute('src')
        imgstring = image_url.split(',')[1]
        imgdata = base64.b64decode(imgstring)
        with open('download.png', 'wb') as f:
            f.write(imgdata)
    def getCaptcha(filename):
        getImage()
        api_url = 'https://api.api-ninjas.com/v1/imagetotext'
        image_file_descriptor = open(filename, 'rb')
        files = {'image': image_file_descriptor}
        Headers = { "X-Api-Key" :  "kVECTAGldECAYKWiqYbnfA==CZDT9FwujKw6dFeD"}
        r = requests.post(api_url,headers=Headers, files=files)
        while True:
            if r.json() != [] and len(r.json()[0]['text']) >= 4:
                break
            driver.find_element(By.XPATH, value='//*[@id="reloadCaptcha"]/i').click()
            getImage()
            image_file_descriptor = open(filename, 'rb')
            files = {'image': image_file_descriptor}
            r = requests.post(api_url,headers=Headers, files=files)
        return r.json()[0]['text']
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.gunnylaumienphi2017.com/")
    time.sleep(1)
    driver.execute_script("window.stop();")
    driver.find_element(By.XPATH, value='//*[@id="global_header"]/ul/li[7]/a/span').click()
    driver.find_element(By.XPATH, value='//*[@id="loginform"]/div[6]/div/div/a').click()


    # Opening JSON file
    path = "E:/ToolStudy/Test/data.json"
    f = open(path)

    # Parse the JSON data
    data = json.load(f)

    num = data['id']
    if num == 100:
        driver.quit()
        sys.exit()
    UserName = data['UserName']
    Password = data['Password']
    Email = data['Email']
    Phone = data['Phone']

    Captcha = getCaptcha(filename='download.png')[:4]

    driver.find_element(By.XPATH, value='//*[@id="UserNameReg"]').send_keys(UserName+ str(num))
    driver.find_element(By.XPATH, value='//*[@id="PasswordReg"]').send_keys(Password)
    driver.find_element(By.XPATH, value='//*[@id="Email"]').send_keys(Email+ str(num) + "@gmail.com")
    driver.find_element(By.XPATH, value='//*[@id="Phone"]').send_keys(Phone)
    driver.find_element(By.XPATH, value='//*[@id="Captcha"]').send_keys(Captcha.upper())
    driver.find_element(By.XPATH, value='//*[@id="btn-signup"]').click()
    time.sleep(1)

    if driver.find_element(By.XPATH, value='/html/body/app-root/div[1]/div[1]/ul/li[3]/a/span').text==UserName+ str(num):
        num += 1
    dictionary = {
        "id": num,
        "UserName": UserName,
        "Password": Password,
        "Email": UserName,
        "Phone": "0329690201"
    }
    with open(path, 'w') as f1:
        json.dump(dictionary, f1)
    f.close()
    driver.quit()






