from selenium import webdriver
from time import sleep
import csv
from page2 import Details_Scrape
from pyvirtualdisplay import Display
from sys import argv
from cityscrape import *

class Company_Scrape:
    def __init__(self,url,*args,**kwargs):
        self.url=url#'https://angel.co/companies'
        #PROXY = '80.191.174.220:8080'
        #chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--proxy-server=%s' % PROXY)
        self.driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')#,options=chrome_options)
        self.driver.set_window_size(1920,1080)
        self.captcha_xpath="//iframe"
        #do it while more is present!!
        self.more_xpath="//div[@class='more']"
        self.company_name_xpath="//div[@class='name']//a"
        self.table_xpath="//div[@class=' dc59 frw44 _a _jm']"
        #check for is header path is >=9 or not
        self.header_xpath="//div[@class='base header']//div"
        self.all_value_except_company="//div[@class='value']"
        
        
    def captcha_solve(self):
        try:
            element=self.driver.find_element_by_xpath(self.captcha_xpath)
            element.click()
        except:
            self.more_click()

    def more_click(self):
        while True:
            try:
                sleep(5)
                element=self.driver.find_element_by_xpath(self.more_xpath)
                element.click()
            except Exception as e:
                print(e)
                break

    def table_data(self):
        company_element = self.driver.find_elements_by_xpath(self.company_name_xpath)
        company_list=[]
        for company in company_element:
            tup=(company.text,company.get_attribute('href'))
            company_list.append(tup)

        details_scrape=Details_Scrape()
        details_scrape.setdata(company_list,self.driver)
        details_scrape.company_details()
            

    def run(self):
        
        try:
            self.driver.get(self.url)
            self.captcha_solve()
            self.more_click()
            self.table_data()
            
        except:
            self.driver.quit()
            raise
        finally:
            self.driver.quit()

if __name__ == '__main__':
    
    
    if '--not-headless' in argv:
        HEADLESS = False
    else:
        HEADLESS = True

    if HEADLESS:
        disp = Display(visible=0, size=(1920,1080))
        disp.start()
    xpath_dict={'cities':"//ul[@class='with-dots']//li//div//a"}
    base_url='https://angel.co/companies?keywords='
    url='https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068'
    data=makeurl(xpath_dict,url,base_url)
    
    urllist=[
        'https://angel.co/companies?company_types[]=Startup',
        'https://angel.co/companies?company_types[]=Private+Company',
        ]
    urllist+=data
    for url in urllist:
        Company_Scrape(url).run()
    if HEADLESS:
        disp.stop()


