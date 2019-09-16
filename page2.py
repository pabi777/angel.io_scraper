from selenium import webdriver
from time import sleep
import csv
import os
class Details_Scrape:
    def __init__(self,company_name,company_url):
        self.employe_xpath="//h4[@class='__halo_textContrast_dark_AAAA __halo_fontSizeMap_size--lg __halo_fontWeight_medium styles_component__1kg4S name_9d036']"
        self.designation_xpath="//h4[@class='__halo_textContrast_dark_AAAA __halo_fontSizeMap_size--lg __halo_fontWeight_medium styles_component__1kg4S name_9d036']/following-sibling::span"
        self.driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        self.company_name=company_name
        self.url=company_url
        self.table_keys="//dd"
        self.table_values="//dt"
        self.people_click="//a[@title='People']"
        self.get_url(self.url)
    
    def get_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e)
            self.get_url(url)

    def getheader(self,filename,fieldnames):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    
    def csv_row_writer(self,filename,fieldnames,datadict):
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(datadict)

    def people(self):
        self.get_url(self.url+'/people')
        employe_element=self.driver.find_elements_by_xpath(self.employe_xpath)
        #print([ele.text for ele in employe_element])
        designation_element=self.driver.find_elements_by_xpath(self.designation_xpath)
        datadict=dict(zip([ele.text for ele in employe_element],[ele.text for ele in designation_element]))

        
    def table_data(self):
        table_keys=self.driver.find_elements_by_xpath(self.table_keys)
        #print([ele.text for ele in employe_element])
        table_values=self.driver.find_elements_by_xpath(self.table_values)
        datadict=dict(zip([ele.text for ele in table_keys],[ele.text for ele in table_values]))



Details_Scrape().do()