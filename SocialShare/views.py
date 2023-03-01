from django.shortcuts import render
from django import template
from .models import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 
import random
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests


# Create your views here.

def home(request):
    return render(request, 'home.html')

def insta_com(request):
    PATH = 'chromedriver.exe'

    #Handling of Allow Pop Up In Facebook
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    #maximizing the window
    driver.maximize_window()

    #navigating to instagram page
    driver.get("https://www.instagram.com/")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id to store email
    id = Credential.objects.values('username')
    id = (id[0]["username"])
    #passing email to email input box
    driver.find_element("xpath",'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(id)

    #creating password to store password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    #passing password to password input box
    driver.find_element("xpath",'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)

    #clicking the login button
    driver.find_element("xpath","//button[@type='submit']").click()
    time.sleep(3)

    driver.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    time.sleep(3)

    #click on explore tab
    driver.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[3]/div/a/div/div[2]/div/div').click()
    time.sleep(3)

    #posting multiple comments in explore
    comment_list=Comment.objects.all()
    print(comment_list)
    for i in range(1,3):
        driver.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div['+str(i)+']/div[2]/div/a/div').click()
        time.sleep(13)
        driver.find_element('xpath','/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea').click()
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea').send_keys(random.choice(comment_list))
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]/div').click()
        time.sleep(3)
        for i in range(1,3):
            print(i)
            driver.find_element('xpath','/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div['+str(i)+']/button').click()
            time.sleep(3)
            driver.find_element('xpath','/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea').click()
            time.sleep(3)
            driver.find_element('xpath','/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea').send_keys(random.choice(comment_list))
            time.sleep(3)
            driver.find_element('xpath','/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]/div').click()
            time.sleep(3)
        driver.find_element('xpath','/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div').click()
        time.sleep(3)
    time.sleep(5)
    driver.close()

def insta_msg(request):
    PATH = 'chromedriver.exe'

    #Handling of Allow Pop Up In Facebook
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    #maximizing the window
    driver.maximize_window()

    #navigating to instagram page
    driver.get("https://www.instagram.com/")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id to store email
    id = Credential.objects.values('username')
    id = (id[0]["username"])
    #passing email to email input box
    driver.find_element("xpath",'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(id)

    #creating password to store password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    #passing password to password input box
    driver.find_element("xpath",'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)

    #clicking the login button
    driver.find_element("xpath","//button[@type='submit']").click()
    time.sleep(3)

    driver.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    time.sleep(3)

    # posting messages to our followings
    msg_list = Message.objects.all()
    print(msg_list)
    for i in range(1,4):
        driver.get('https://www.instagram.com/direct/inbox/')
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div/div/div/div['+str(i)+']/div/a/div/div[2]').click()
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(random.choice(msg_list))
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
        time.sleep(3)
    time.sleep(5)
    driver.close()

def fb_post(request):
    # getting api
    api='https://lifeideology.com/liapi/v1/blog/post/'
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("sucessfully fetched the data with parameters provided")
        data = response.json()['results'][0]
        meta_description = data['meta_description']
        print(meta_description)
        title = data['title']
        print(title)
        tag = ('#'+response.json()['results'][0]['tag'][0]['title'])
        tag = tag.replace(" ", "")
        print(tag)
        slug = data['slug']
        url = 'https://lifeideology.com/blog/'+slug
        print(url)
        featured = data['featured']
        print(featured)
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")


    PATH = 'chromedriver.exe'

    #Handling of Allow Pop Up In Facebook
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id to store email id
    id = Credential.objects.values('email')
    id = (id[0]["email"])
    #passing email to email box
    driver.find_element('id','email').send_keys(id)

    #creating password to store the password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    #passing password to password box
    driver.find_element('id','pass').send_keys(password)

    #clicking the login button
    driver.find_element('name','login').click()
    time.sleep(3)

    driver.get('https://www.facebook.com/')
    time.sleep(3)

    #posting post on fb
    driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span').click()
    time.sleep(3)

    post=(url +'\n'+ meta_description +'\n'+ tag +'\n'+ featured)
    driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[6]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/p').send_keys(post)
    time.sleep(3)

    driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[6]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div').click()
    time.sleep(3)

    driver.get('https://www.facebook.com/')
    time.sleep(3)

    sleep(5)
    driver.close()

def fb_com(request):
    PATH = 'chromedriver.exe'

    #Handling of Allow Pop Up In Facebook
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id to store email id
    id = Credential.objects.values('email')
    id = (id[0]["email"])
    #passing email to email box
    driver.find_element('id','email').send_keys(id)

    #creating password to store the password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    #passing password to password box
    driver.find_element('id','pass').send_keys(password)

    #clicking the login button
    driver.find_element('name','login').click()
    time.sleep(3)

    driver.get('https://www.facebook.com/')
    time.sleep(3)

    #posting comments on multiple post
    comment_list=Comment.objects.all()
    print(comment_list)
    for i in range(1,4):
        a = str(i)
        try:
            driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div/div[3]/div/div[3]/div/div/div['+a+']/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div[1]/div/div/div/div[2]').click()
            time.sleep(3)
        except:
            continue
        comment=random.choice(comment_list)
        a = driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div/div[3]/div/div[3]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/form/div/div/div[1]/div/div[1]/p')
        a.send_keys(comment)
        a.send_keys(Keys.ENTER)
        time.sleep(3)
    sleep(5)
    driver.close()

def fb_msg(request):
    PATH = 'chromedriver.exe'

    #Handling of Allow Pop Up In Facebook
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id to store email id
    id = Credential.objects.values('email')
    id = (id[0]["email"])
    #passing email to email box
    driver.find_element('id','email').send_keys(id)

    #creating password to store the password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    #passing password to password box
    driver.find_element('id','pass').send_keys(password)

    #clicking the login button
    driver.find_element('name','login').click()
    time.sleep(3)

    driver.get('https://www.facebook.com/')
    time.sleep(3)

    # posting messages to our friends
    msg_list = Message.objects.all()
    print(msg_list)
    for i in range(4,7):
        driver.get('https://www.facebook.com/friends/list')
        time.sleep(3)
        try:
            driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div['+str(i)+']/a/div[1]/div[2]').click()
            time.sleep(3)
        except:
            continue
        try:
            driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[1]/div[2]').click()
            time.sleep(3)
        except:
            continue
        driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[7]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p').send_keys(random.choice(msg_list))
        time.sleep(3)      
        driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[7]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div').click()
        time.sleep(3)
    sleep(5)
    driver.close()

def fb_grp_post(request):
    # getting api
    api='https://lifeideology.com/liapi/v1/blog/post/'
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("sucessfully fetched the data with parameters provided")
        data = response.json()['results'][0]
        meta_description = data['meta_description']
        print(meta_description)
        title = data['title']
        print(title)
        tag = ('#'+response.json()['results'][0]['tag'][0]['title'])
        tag = tag.replace(" ", "")
        print(tag)
        slug = data['slug']
        url = 'https://lifeideology.com/blog/'+slug
        print(url)
        featured = data['featured']
        print(featured)
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")


    PATH = 'chromedriver.exe'

    #Handling of Allow Pop Up In Facebook
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id to store email id
    id = Credential.objects.values('email')
    id = (id[0]["email"])
    #passing email to email box
    driver.find_element('id','email').send_keys(id)

    #creating password to store the password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    #passing password to password box
    driver.find_element('id','pass').send_keys(password)

    #clicking the login button
    driver.find_element('name','login').click()
    time.sleep(3)

    driver.get('https://www.facebook.com/')
    time.sleep(3)

    # sending posts on groups we follow
    post=(url +'\n'+ meta_description +'\n'+ tag +'\n'+ featured)
    for i in range(1,5):
        driver.get('https://www.facebook.com/')
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[3]/div[3]/div/div[1]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div/span/div/div/div[3]').click()
        time.sleep(3)
        try:
            driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div['+str(i)+']/div/div/a/div[1]').click()
            time.sleep(3)
            print(i)
        except:
            continue
        try:
            driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[2]/div[1]/div/div[2]/div/div/div[4]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]').click()
            time.sleep(3)
        except:
            continue
        driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[6]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(post)
        time.sleep(5)
        driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[6]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]').click()
        time.sleep(5)
    sleep(5)
    driver.close()


def disqus_com(request):
    #Handling of Allow Pop Up In Disqus
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    
    PATH = 'chromedriver.exe'
    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    driver.maximize_window()

    #login google account
    driver.get('https://accounts.google.com/')
    email = Credential.objects.values('email')
    email = (email[0]["email"])
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(email)
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(password)
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(3)

    #login disqus using google account
    driver.get("https://disqus.com/profile/login/")
    driver.find_element('xpath','/html/body/section/form/div[2]/button[3]/span/img').click()
    time.sleep(3)
    driver.find_element('xpath','/html/body/div/div/div[2]/div/div/div/div/p/a[1]').click()
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/a[1]/div/p').click()
    time.sleep(3)

    for i in range(1,5):
        driver.get('https://disqus.com/home/')
        time.sleep(3)
        a = str(i)
        try:
            driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[2]/div/div/section/div[4]/div/div[2]/div/div['+a+']/div[3]/div/div[3]/ul/li[2]/a').click()
            print(a)                     
        except:
            print(a +' element not found')
            continue
        time.sleep(3)
        comment_list = Comment.objects.all()
        print(comment_list)
        src = driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div/div/section/div/div/iframe[1]').get_attribute('src')
        print(src)
        time.sleep(3)
        driver.get(src)
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[3]/div/div/div/section/div/div[1]/form/div/div[3]/div[2]/div/div[1]/span').click()
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[3]/div/div/div/section/div/div[1]/form/div/div[3]/div[2]/div/div[1]/div[1]').send_keys(random.choice(comment_list))
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[3]/div/div/div/section/div/div[1]/form/div/div[3]/div[2]/div/div[5]/div/div[2]/section/div/button[1]').click()
        time.sleep(3)

    print('loop terminated')
    sleep(5)
    driver.close()

def li_post(request):
    # getting api
    api='https://lifeideology.com/liapi/v1/blog/post/'
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("sucessfully fetched the data with parameters provided")
        data = response.json()['results'][0]
        meta_description = data['meta_description']
        print(meta_description)
        title = data['title']
        print(title)
        tag = ('#'+response.json()['results'][0]['tag'][0]['title'])
        tag = tag.replace(" ", "")
        print(tag)
        slug = data['slug']
        url = 'https://lifeideology.com/blog/'+slug
        print(url)
        featured = data['featured']
        print(featured)
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")

    PATH = 'chromedriver.exe'

    #Handling of Allow Pop Up In Facebook
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    #creating driver object
    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    #maximizing the window
    driver.maximize_window()

    #navigating to linkedin page
    driver.get("https://in.linkedin.com/")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id to store email id
    id = Credential.objects.values('email')
    id = (id[0]["email"])
    #passing email to email box
    driver.find_element('xpath','//*[@id="session_key"]').send_keys(id)

    #creating password to store the password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    #passing password to password box
    driver.find_element('xpath','//*[@id="session_password"]').send_keys(password)

    #clicking the login button
    driver.find_element('xpath',"//button[@class='sign-in-form__submit-button']").click()
    time.sleep(20)
        
    driver.find_element('xpath','/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/section/div[2]/div/a[2]/div').click()
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[5]/div[3]/div/div[3]/div[2]/div[1]/div[3]/div/div[2]/main/div/div[1]/div/div/div[1]/button/span').click()
    time.sleep(3)

    post=(api.url +'\n'+ api.meta_description +'\n'+ api.tag +'\n'+ api.featured)
    driver.find_element('xpath','/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[1]/p').send_keys(post)
    time.sleep(3)

    driver.find_element('xpath','/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[4]/button').click()
    time.sleep(3)
    sleep(5)
    driver.close()

def li_grp_post(request):
    # getting api
    api='https://lifeideology.com/liapi/v1/blog/post/'
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("sucessfully fetched the data with parameters provided")
        data = response.json()['results'][0]
        meta_description = data['meta_description']
        print(meta_description)
        title = data['title']
        print(title)
        tag = ('#'+response.json()['results'][0]['tag'][0]['title'])
        tag = tag.replace(" ", "")
        print(tag)
        slug = data['slug']
        url = 'https://lifeideology.com/blog/'+slug
        print(url)
        featured = data['featured']
        print(featured)
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")

    PATH = 'chromedriver.exe'

    #Handling of Allow Pop Up In Facebook
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    #creating driver object
    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    #maximizing the window
    driver.maximize_window()

    #navigating to linkedin page
    driver.get("https://in.linkedin.com/")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id to store email id
    id = Credential.objects.values('email')
    id = (id[0]["email"])
    #passing email to email box
    driver.find_element('xpath','//*[@id="session_key"]').send_keys(id)

    #creating password to store the password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    #passing password to password box
    driver.find_element('xpath','//*[@id="session_password"]').send_keys(password)

    #clicking the login button
    driver.find_element('xpath',"//button[@class='sign-in-form__submit-button']").click()
    time.sleep(20)
        
    # posting posts on groups in linkedin
    for i in range(1,5):
        driver.get('https://www.linkedin.com/groups/')
        time.sleep(3)
        try:
            driver.find_element('xpath','/html/body/div[5]/div[3]/div/div[2]/div/div/main/div/div/div[2]/div[2]/div[1]/div/ul/li['+str(i)+']/div/div/div[1]/div[2]/div[1]/a').click()
            time.sleep(3)
        except:
            continue
        driver.find_element('xpath','/html/body/div[5]/div[3]/div/div[2]/div/div/main/div/div[5]/div/div[1]/button').click()
        time.sleep(3)
        post=(api.url +'\n'+ api.meta_description +'\n'+ api.tag +'\n'+ api.featured)
        driver.find_element('xpath','/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[1]/p').send_keys(post)
        time.sleep(5)
        driver.find_element('xpath','/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[3]/button').click()
        time.sleep(3)
    sleep(5)
    driver.close()

def li_com(request):
    PATH = 'chromedriver.exe'

    #Handling of Allow Pop Up In Facebook
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    #creating driver object
    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    #maximizing the window
    driver.maximize_window()

    #navigating to linkedin page
    driver.get("https://in.linkedin.com/")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id to store email id
    id = Credential.objects.values('email')
    id = (id[0]["email"])
    #passing email to email box
    driver.find_element('xpath','//*[@id="session_key"]').send_keys(id)

    #creating password to store the password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    #passing password to password box
    driver.find_element('xpath','//*[@id="session_password"]').send_keys(password)

    #clicking the login button
    driver.find_element('xpath',"//button[@class='sign-in-form__submit-button']").click()
    time.sleep(20)
        
    # posting comments in linkedin
    comment_list = Comment.objects.all()
    print(comment_list)
    driver.get('https://www.linkedin.com/groups/')
    for i in range(1,5):
        driver.get('https://www.linkedin.com/groups/')
        time.sleep(3)
        try:
            driver.find_element('xpath','/html/body/div[5]/div[3]/div/div[2]/div/div/main/div/div/div[2]/div[2]/div[1]/div/ul/li['+str(i)+']/div/div/div[1]/div[2]/div[1]/a').click()
            time.sleep(3)
        except:
            continue
        for j in range(1,10):
            driver.execute_script("window.scrollTo(0, 300)")
            try:
                driver.find_element('xpath','/html/body/div[5]/div[3]/div/div[2]/div/div/main/div/div[6]/div[1]/div/div['+str(j)+']/div/div/div/div/div[5]/div[2]/span[2]/span/div[1]/button').click()
                time.sleep(3)
                print(j)
            except:
                continue
            driver.find_element('xpath','/html/body/div[5]/div[3]/div/div[2]/div/div/main/div/div[6]/div[1]/div/div['+str(j)+']/div/div/div/div/div[5]/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p').send_keys(random.choice(comment_list))
            time.sleep(3)
            driver.find_element('xpath','/html/body/div[5]/div[3]/div/div[2]/div/div/main/div/div[6]/div[1]/div/div['+str(j)+']/div/div/div/div/div[5]/div[3]/div[1]/div[2]/form/div[2]/button').click()
            time.sleep(3)
    sleep(5)
    driver.close()

def quora_post(request):
    # getting api
    api='https://lifeideology.com/liapi/v1/blog/post/'
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("sucessfully fetched the data with parameters provided")
        data = response.json()['results'][0]
        meta_description = data['meta_description']
        print(meta_description)
        title = data['title']
        print(title)
        tag = ('#'+response.json()['results'][0]['tag'][0]['title'])
        tag = tag.replace(" ", "")
        print(tag)
        slug = data['slug']
        url = 'https://lifeideology.com/blog/'+slug
        print(url)
        featured = data['featured']
        print(featured)
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")

    PATH = 'chromedriver.exe'
    #Handling of Allow Pop Up In Quora
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    driver.maximize_window()

    #login google account
    driver.get('https://accounts.google.com/')
    email = Credential.objects.values('email')
    email = (email[0]["email"])
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(email)
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(password)
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(3)

    #navigating to quora page
    driver.get("https://www.quora.com/")
    time.sleep(3)

    #login quora using google account
    driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div').click()
    time.sleep(3)

    #creating post
    driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div[3]/button/div/div[2]/div').click()
    time.sleep(3)

    a = driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div/div/div')
    if(a.text):
        driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div').clear()
        time.sleep(3)

    post=(api.url +'\n'+ api.meta_description +'\n'+ api.tag +'\n'+ api.featured)
    driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div').send_keys(post)
    time.sleep(3)

    driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/button/div/div/div').click()
    time.sleep(5)
    driver.close()

def quora_post_spaces(request):
    # getting api
    api='https://lifeideology.com/liapi/v1/blog/post/'
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("sucessfully fetched the data with parameters provided")
        data = response.json()['results'][0]
        meta_description = data['meta_description']
        print(meta_description)
        title = data['title']
        print(title)
        tag = ('#'+response.json()['results'][0]['tag'][0]['title'])
        tag = tag.replace(" ", "")
        print(tag)
        slug = data['slug']
        url = 'https://lifeideology.com/blog/'+slug
        print(url)
        featured = data['featured']
        print(featured)
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")

    PATH = 'chromedriver.exe'
    #Handling of Allow Pop Up In Quora
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    driver.maximize_window()

    #login google account
    driver.get('https://accounts.google.com/')
    email = Credential.objects.values('email')
    email = (email[0]["email"])
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(email)
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(password)
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(3)

    #navigating to quora page
    driver.get("https://www.quora.com/")
    time.sleep(3)

    #login quora using google account
    driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div').click()
    time.sleep(3)

    post=(api.url +'\n'+ api.meta_description +'\n'+ api.tag +'\n'+ api.featured)
    
    #creating posts for spaces
    for i in range(1,4):
        driver.get("https://www.quora.com/")
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]').click()
        time.sleep(3)
        a = str(i)
        driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[3]/a['+a+']/div/div/div[2]/div[1]/div').click()
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[4]/div/div/div[1]/div[2]/div/div[2]').click()
        time.sleep(3)
        b = driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/div[1]/div')
        if(b.text):
            driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/div[1]/div').clear()
            time.sleep(3)
        c = driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/div[1]/div').get_attribute('data-placeholder')
        if c:
            driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div').send_keys(post)
        else:    
            driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div/textarea').send_keys(post)
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/button[2]/div/div/div').click()
    time.sleep(5)
    driver.close()

def quora_com(request):
    PATH = 'chromedriver.exe'
    #Handling of Allow Pop Up In Quora
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    driver.maximize_window()

    #login google account
    driver.get('https://accounts.google.com/')
    email = Credential.objects.values('email')
    email = (email[0]["email"])
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(email)
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(password)
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(3)

    #navigating to quora page
    driver.get("https://www.quora.com/")
    time.sleep(3)

    #login quora using google account
    driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div').click()
    time.sleep(3)

    # comment on multiple posts of each space
    comment_list = Comment.objects.all()
    print(comment_list)
    for j in range(1,4):
        driver.get("https://www.quora.com/")
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]').click()
        time.sleep(3)
        a = str(j)
        driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[3]/a['+a+']/div/div/div[2]/div[1]/div').click()
        time.sleep(3)
        a = 500
        for i in range(1,6):
            driver.execute_script("window.scrollTo(0, "+str(a)+")")
            a = a + 600
            time.sleep(5)
            try:
                driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[5]/div/div/div[1]/div[4]/div/div/div['+str(i)+']/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[1]/div[2]/div/div/div/button').click()
                time.sleep(3)
            except:
                continue
            driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[5]/div/div/div[1]/div[4]/div/div/div['+str(i)+']/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div/div/div[1]/div/div').send_keys(random.choice(comment_list))
            time.sleep(3)
            driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[5]/div/div/div[1]/div[4]/div/div/div['+str(i)+']/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(3)
    time.sleep(5)
    driver.close()

def reddit_post(request):
    # getting api
    api='https://lifeideology.com/liapi/v1/blog/post/'
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("sucessfully fetched the data with parameters provided")
        data = response.json()['results'][0]
        meta_description = data['meta_description']
        print(meta_description)
        title = data['title']
        print(title)
        tag = ('#'+response.json()['results'][0]['tag'][0]['title'])
        tag = tag.replace(" ", "")
        print(tag)
        slug = data['slug']
        url = 'https://lifeideology.com/blog/'+slug
        print(url)
        featured = data['featured']
        print(featured)
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")

    PATH = 'chromedriver.exe'
    #Handling of Allow Pop Up In Reddit
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    driver.maximize_window()

    #navigating to Reddit page
    driver.get("https://www.reddit.com/login/")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id to store email id
    id = Credential.objects.values('username')
    id = (id[0]["username"])
    #passing email to email box
    driver.find_element('id','loginUsername').send_keys(id)

    #creating password to store the password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    #passing password to password box
    driver.find_element('id','loginPassword').send_keys(password)

    #clicking the login button
    driver.find_element('xpath',"/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").click()
    time.sleep(15)
    driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[4]/div/div/div/header/div/div[2]/button').click()
    time.sleep(3)

    # #post on reddit
    driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[4]/a').click()
    time.sleep(3)

    community='r/announcements'
    driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[1]/input').send_keys(community)
    time.sleep(3)

    title='post'
    driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div/textarea').send_keys(title)
    time.sleep(3)

    post=(api.url +'\n'+ api.meta_description +'\n'+ api.tag +'\n'+ api.featured)
    driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div/div/div/div/div').send_keys(post)
    time.sleep(3)

    driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div/div[1]/button').click()
    time.sleep(3)
    sleep(5)
    driver.close()

def reddit_com(request):
    PATH = 'chromedriver.exe'
    #Handling of Allow Pop Up In Reddit
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    driver.maximize_window()

    #navigating to Reddit page
    driver.get("https://www.reddit.com/login/")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id to store email id
    id = Credential.objects.values('username')
    id = (id[0]["username"])
    #passing email to email box
    driver.find_element('id','loginUsername').send_keys(id)

    #creating password to store the password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    #passing password to password box
    driver.find_element('id','loginPassword').send_keys(password)

    #clicking the login button
    driver.find_element('xpath',"/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").click()
    time.sleep(15)
    driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[4]/div/div/div/header/div/div[2]/button').click()
    time.sleep(3)

    #posting comments in reddit
    comment_list = Comment.objects.all()
    print(comment_list)
    for j in range(1,4):
        driver.get('https://www.reddit.com/best/')
        driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/header/div/div[1]/div[2]/button').click()
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/header/div/div[1]/div[2]/div/a['+str(j)+']').click()
        time.sleep(10)
        for i in range(1,5):
            try:
                driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div[1]/div[5]/div['+str(i)+']/div/div/div[3]/div[4]/div[2]/a').click()
                time.sleep(3)
            except:
                continue 
            driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[3]/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div/div').send_keys(random.choice(comment_list))
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, 300)")
            driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/button').click()
            time.sleep(5)
            driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/header/div/div[1]/div[1]/button').click()
            time.sleep(3)
            driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/header/div/div[1]/div[1]/div/a['+str(j)+']').click()
            time.sleep(10)
    sleep(5)
    driver.close()

def twitter_post(request):
    # getting api
    api='https://lifeideology.com/liapi/v1/blog/post/'
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("sucessfully fetched the data with parameters provided")
        data = response.json()['results'][0]
        meta_description = data['meta_description']
        print(meta_description)
        title = data['title']
        print(title)
        tag = ('#'+response.json()['results'][0]['tag'][0]['title'])
        tag = tag.replace(" ", "")
        print(tag)
        slug = data['slug']
        url = 'https://lifeideology.com/blog/'+slug
        print(url)
        featured = data['featured']
        print(featured)
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")

    PATH = 'chromedriver.exe'

    #Handling of Allow Pop Up In Facebook
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    #creating driver object
    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    #maximizing the window
    driver.maximize_window()

    #navigating to twitter page
    driver.get("https://twitter.com/login?lang=en-gb")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id for storing email,phone,or username
    id = Credential.objects.values('username')
    id = (id[0]["username"])
    #passing id to the id box
    driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(id)

    #clicking on next button
    driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()

    #creating password for storing password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    time.sleep(3)
    #passing password to password box
    driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password)

    #clicking the login button
    driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
    time.sleep(3)

    #posting tweet
    driver.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
    time.sleep(3)

    post=(api.title +'\n'+ api.url +'\n'+ api.tag +'\n')
    driver.find_element('xpath','//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(post)
    time.sleep(3)

    driver.find_element('xpath','//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]').click()
    time.sleep(3)
    sleep(5)
    driver.close()

def twitter_com(request):
    PATH = 'chromedriver.exe'

    #Handling of Allow Pop Up In Facebook
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    #creating driver object
    driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
    #maximizing the window
    driver.maximize_window()

    #navigating to twitter page
    driver.get("https://twitter.com/login?lang=en-gb")

    #delaying for 3 seconds so that the email and password boxes can load
    time.sleep(3)

    #creating id for storing email,phone,or username
    id = Credential.objects.values('username')
    id = (id[0]["username"])
    #passing id to the id box
    driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(id)

    #clicking on next button
    driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()

    #creating password for storing password
    password = Credential.objects.values('password')
    password = (password[0]["password"])
    time.sleep(3)
    #passing password to password box
    driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password)

    #clicking the login button
    driver.find_element('xpath','//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
    time.sleep(3)

    driver.get('https://twitter.com/home')
    time.sleep(3)
    comment_list = Comment.objects.all()
    print(comment_list)
    for i in range(1,4):
        driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[6]/div').click()
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/div').click()
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div/div[2]').click()
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div[2]/div[4]/div[1]/a').click()
        time.sleep(3)
        driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div['+str(i)+']/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]').click()
        time.sleep(3)
        for j in range(1,5):
            try:
                driver.find_element('xpath','/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div['+str(j)+']/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]').click()
                time.sleep(3)
                print(j)
            except:
                continue
            driver.execute_script("window.scrollTo(0, 300)")
            flag = 0
            try:
                driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(random.choice(comment_list))
                flag = 1
                time.sleep(3)
            except:
                print('no comments')
            if(flag == 1):
                driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]').click()
                time.sleep(3)
            else:
                try:
                    driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]').click()
                    time.sleep(3)
                except:
                    continue
                driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(random.choice(comment_list))
                time.sleep(3)
                driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]').click()
                time.sleep(3)
                driver.find_element('xpath','/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div').click()
                time.sleep(3)
    sleep(5)
    driver.close()
