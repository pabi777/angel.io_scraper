from selenium import webdriver
from time import sleep
import csv
import os
import json


class Details_Scrape:
    def __init__(self):
        self.company_data_list=[]
        self.company_dict={}

    def setdata(self,company_tups,driver): #(company_name,company_url)
        self.employe_xpath="//h4[@class='__halo_textContrast_dark_AAAA __halo_fontSizeMap_size--lg __halo_fontWeight_medium styles_component__1kg4S name_9d036']"
        self.designation_xpath="//h4[@class='__halo_textContrast_dark_AAAA __halo_fontSizeMap_size--lg __halo_fontWeight_medium styles_component__1kg4S name_9d036']/following-sibling::span"
        self.driver=driver #webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        self.investors="//h4[@class='__halo_textContrast_dark_AAAA __halo_fontSizeMap_size--lg __halo_fontWeight_medium styles_component__1kg4S name_9d036']//a"
        self.table_keys="//dd"
        self.table_values="//dt"
        for company,url in company_tups:
            self.get_url(url)
            self.company_dict.update({'company':company})
            self.company_details()
            self.people(url)
            self.investors_fetch(url)
            self.csv_row_writer()
            self.company_dict.clear()
            
            
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


    def csv_row_writer(self,filename='US.json'):
        if not os.path.isfile(filename):
            with open(filename, 'w') as txtfile:
                pass
            
        with open(filename, 'a') as txtfile:
            jsondata=json.dumps(self.company_dict,indent=4)
            json.dump(jsondata,txtfile)
            
            

    def people(self,url):
        self.get_url(url+'/people')
        employe_element=self.driver.find_elements_by_xpath(self.employe_xpath)
        #print([ele.text for ele in employe_element])
        designation_element=self.driver.find_elements_by_xpath(self.designation_xpath)
        datadict=dict(zip([ele.text for ele in employe_element],[ele.text for ele in designation_element]))
        self.company_dict.update(datadict)
        #print(self.company_dict)

    def company_details(self):
        try:
            sleep(2)
            table_keys=self.driver.find_elements_by_xpath(self.table_keys)
            #print([ele.text for ele in employe_element])
            table_values=self.driver.find_elements_by_xpath(self.table_values)
            datadict=dict(zip([ele.text for ele in table_keys],[ele.text for ele in table_values]))
            #print([ele.text for ele in table_keys],[ele.text for ele in table_values])
            self.company_dict.update(datadict)
            #print(self.company_dict)
        except Exception as e:
            print(e)

    def investors_fetch(self,url):
        try:
            self.get_url(url+'/funding')
            investors_name_element=self.driver.find_elements_by_xpath(self.investors)
            investors_name=[self.company_dict.update({name.text:'investors'}) for name in investors_name_element ]
        except Exception as e:
            print(e)




#Details_Scrape().do()
