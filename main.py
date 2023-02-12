from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager      #use if driver is not installed into system.
import time


for i in range(20):
  
    driver=webdriver.Chrome() 
    #driver = webdriver.Chrome(ChromeDriverManager().install())    #use if driver is not installed into system.
    
    driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]').send_keys('xxxx8546xx')
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input').click()
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[1]/div[1]/div[2]/a').click()
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/form/span/span/input').click()
    driver.close()
