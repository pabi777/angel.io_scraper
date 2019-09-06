from selenium import webdriver
from time import sleep

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
                element=self.driver.find_element_by_xpath(self.more_xpath)
                element.click()
            except:
                sleep(12)
                self.driver.get(self.url)
                self.run()
            if element:
                yield True
            else:
                break

    def get_header(self):
        pass

    def run(self):
        self.driver.get(self.url)
        self.captcha_solve()
        self.more_click()
        self.driver.quit()

Company_Scrape().run()