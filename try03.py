
# code 1


# from bs4 import BeautifulSoup    
# import urllib.request 
# url = urllib.request.urlopen("https://seomagnifier.com/online-paraphrasing-tool")    
# content = url.read()    
# # print(content)
# soup = BeautifulSoup(content,'html.parser')
# print(soup)


# code 2

# import urllib.request
# from bs4 import BeautifulSoup

# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

# url = "https://www.prepostseo.com/paraphrasing-tool"
# headers={'User-Agent':user_agent,} 

# request=urllib.request.Request(url,None,headers) #The assembled request
# response = urllib.request.urlopen(request)
# data = response.read() # The data u need
# soup = BeautifulSoup(data,'html.parser')
# print(soup)


# code 3

# from urllib.request import Request, urlopen

# req = Request('https://www.prepostseo.com/paraphrasing-tool', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
# soup = BeautifulSoup(webpage)
# # print(soup)
# results = soup.find(id='input-content')
# print(results.prettify())


# code 4

# from selenium import webdriver
# import time

# # options = webdriver.ChromeOptions()
# # options.add_argument('--ignore-certificate-errors')
# # options.add_argument("--test-type")
# # options.binary_location = "/usr/bin/chromium"
# driver = webdriver.Chrome()#chrome_options=options)

# # driver = webdriver.Chrome()
# driver.get("https://quillbot.com/")
# text_area = driver.find_element_by_id('input-content')
# text_area.send_keys("This text is send using Python code.")
# # button = driver.find_element_by_id('buttonID')
# # button.click()


# code 5

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Firefox()
# url = "https://quillbot.com/"
# text = "Hello hello hello, this is a test"

# driver.get(url)
# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.ID, "input-content"))
# )  # Wait until the `input-content` element appear (up to 5 seconds)
# driver.find_element_by_id("input-content").clear()
# driver.find_element_by_id('input-content').send_keys(text) 


from webbot import Browser 
web = Browser()
web.go_to('https://seomagnifier.com/online-paraphrasing-tool') 
# web.click('Sign in')
print("opened the site")
web.type('krushna patil stay in nashik' , id='data')
print("it should write in to the box")
web.click(id="checkButton")#id="newone",classname="btn.btn-success.btn-lg.newsession" )
print("after click")
# web.type('mypassword' , into='Password' , id='passwordFieldId') # specific selection
# web.click('NEXT' , tag='span') # you are logged in ^_^

