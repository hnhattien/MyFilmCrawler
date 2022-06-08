from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium
import time
import sys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
options = Options()


driver = ""
class PhimmoiCrawler : 
    
    def __init__(self,url) -> None:
        global driver
        options = Options()
        driver = webdriver.Chrome(executable_path=r"C:\Users\Sun\Desktop\chromedriver", chrome_options=options)
        driver.get(url)
    
   
    def interactSiteToAjaxCome(self,count_times):
        global driver
        for i in range(0,count_times) :
           driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
           time.sleep(1)
    def GoIntoFilm(self) : 
        global driver
        print("Hi "+sys.argv[1])
        index = sys.argv[1] or input("Type a index to start from")
        films_item = driver.find_elements_by_css_selector(".blog-wrapper .post-item")
        for i in range(int(index),len(films_item)) :
           films_item.__getitem__(int(i)).click()
           self.getFilmData()
           return 0
    def getFilmData(self) :
        
        global driver
        self.interactSiteToAjaxCome(1)
        
        
        
        
        while(True) : 
            try : 
                if(driver.find_element_by_tag_name("video-js").click() or driver.execute_script("document.querySelector('video-js').click()")) :
                    return 100
            except :
                x = "Hi"
            
         
        

crawler = PhimmoiCrawler("https://phimmoiizz.net/hanh-dong/")
crawler.interactSiteToAjaxCome(7)
crawler.GoIntoFilm()
