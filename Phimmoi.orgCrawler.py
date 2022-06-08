from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium
import time
import sys
import json
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from browsermobproxy import Server
from ProxyManagerModule import ProxyManager
import pprint
proxy = ProxyManager()
server = proxy.start_server()
client = proxy.start_client()
time.sleep(4)
driver = ""
class PhimmoiCrawler : 
    
    def __init__(self,url) -> None:
        global driver
        global client
        global server
        options = Options()
        
        options.add_argument(f"--proxy-server={client.proxy}")
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path=r"C:\Users\Sun\Desktop\chromedriver", chrome_options=options,desired_capabilities=options.to_capabilities())
        driver.get(url)
        time.sleep(4)
    
   
    def interactSiteToAjaxCome(self,count_times):
        global driver
        for i in range(0,count_times) :
           driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
           time.sleep(1)
    def GoIntoFilm(self) : 
        global driver
        global client
        global server
        print("Hi "+sys.argv[1])
        index = sys.argv[1] or input("Type a index to start from")
        films_item = driver.find_elements_by_css_selector("li.movie-item a")
        film_links = []
        for i in range(int(index),len(films_item)) :
           film_links.append(films_item.__getitem__(int(i)).get_attribute("href")) 
        for i in range(int(index),len(film_links)) :
           driver.get(film_links[i])
           self.interactSiteToAjaxCome(1)
           driver.get(driver.find_element_by_id("btn-film-watch").get_attribute("href"))
           while(True) :
               print("Wait for user click to play video...")
               if input() == "1" :
                   break
           time.sleep(50)
           
           
           self.getFilmsData()
           
    def getFilmsData(self) :
        global client
        global server
        global driver
        time.sleep(15)
        print(client.proxy)
        while(True) : 
            client.new_har()
            time.sleep(5)
            result = json.dumps(client.har)
            data = json.loads(result)

            with open("log/proxy","a") as f :
                try : 
                    print(data['log']['entries'][0]['request']['url'])
                    f.write(data['log']['entries'][0]['request']['url'])
                except : 
                    print("Error to Write")
        
        
        
        
        



crawler = PhimmoiCrawler("https://phimmoii.org/the-loai/hanh-dong.html")
crawler.interactSiteToAjaxCome(9)
crawler.GoIntoFilm()
