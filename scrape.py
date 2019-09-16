from selenium import webdriver
from time import sleep
import csv
from page2.Details_Scrape import do

class Company_Scrape:
    def __init__(self):
        self.url='https://angel.co/companies'
        self.driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        self.captcha_xpath="//iframe"
        #do it while more is present!!
        self.more_xpath="//div[@class='more']"
        self.company_name_xpath="//div[@class='name']//a"
        self.table_xpath="//div[@class=' dc59 frw44 _a _jm']"
        #check for is header path is >=9 or not
        self.header_xpath="//div[@class='base header']//div"
        self.all_value_except_company="//div[@class='value']"
        self.filename = 'firstpage.csv'
        
    def captcha_solve(self):
        try:
            element=self.driver.find_element_by_xpath(self.captcha_xpath)
            element.click()
        except:
            self.more_click()

    def more_click(self):
        while True:
            try:
                sleep(4)
                element=self.driver.find_element_by_xpath(self.more_xpath)
                element.click()
            except Exception as e:
                print(e)
                break

    def get_header(self):
        header_element = self.driver.find_elements_by_xpath(self.header_xpath)
        header_text = [header.text for header in header_element if not header.text=='']
        with open(self.filename,'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header_text)
        return header_text

    def table_data(self):
        company_element = self.driver.find_elements_by_xpath(self.company_name_xpath)
        companies = [(company.text,company.get_attribute('href')) for company in company_element]
        
        header_text = self.get_header()
        header_text.insert(1,'Url')
        

        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header_text)
            writer.writeheader()
        
        rest_of_value_elements = self.driver.find_elements_by_xpath(self.all_value_except_company)
        rest_of_value = [data.text for data in rest_of_value_elements]
        high,low,i=10,0,0
        lenth_of_data=len(rest_of_value)
        header_length=len(header_text)
        print('header text length',header_length)
        while True:
            try:
                print(i,low,high)
                line=rest_of_value[low:high]
                line.insert(0,companies[i][0])
                line.insert(1,companies[i][1])
                
                datadict=dict(zip(header_text,line))
                #print(datadict)
                with open(self.filename, 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=header_text)
                    writer.writerow(datadict)
                
            except Exception as e:
                print(e)
                break
            finally:
                i+=1
                low=high
                high+=header_length

    def run(self):
        urllist=[]
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

Company_Scrape().run()