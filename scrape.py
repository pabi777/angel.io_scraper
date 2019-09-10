from selenium import webdriver
from time import sleep
import csv

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
        
    def captcha_solve(self):
        try:
            element=self.driver.find_element_by_xpath(self.captcha_xpath)
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

    def get_header(self):
        header_element = self.driver.find_elements_by_xpath(self.header_xpath)
        header_text = [header.text for header in header_element if not header.text=='']
        with open('data.csv','w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header_text)
        return header_text

    def table_data(self):
        company_element = self.driver.find_elements_by_xpath(self.company_name_xpath)
        companies = [company.text for company in company_element]
        header_text = self.get_header()
        rest_of_value_elements = self.driver.find_elements_by_xpath(self.table_xpath)
        rest_of_value = [data.text for data in rest_of_value_elements]

        table_data = []
        upper_length = len(rest_of_value)-len(header_text)
        low=0
        high=len(header_text)-1

        for company in companies:
            temp=[]
            while( high <= upper_length ):
                temp=rest_of_value[low:high]
                temp.insert(0,company)
                table_data.append(temp)
                low=high
                high+=high+1
                with open ('data.csv','a') as csvfile:
                    writer=csv.writer(csvfile)
                    writer.writerow(table_data)
                temp.clear()
                
            #print(table_data)


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

Company_Scrape().run()