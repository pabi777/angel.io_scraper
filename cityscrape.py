from selenium import webdriver

def driver_init(proxy=False):
    if proxy:
        PROXY = '80.191.174.220:8080'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')#,options=chrome_options)
    driver.set_window_size(1920,1080)
    return driver

def scrape(xpath_dict,url):
    '''
        returns dict
    '''
    driver=driver_init()
    driver.get(url)
    datadict={}
    for key in xpath_dict:
        elements=driver.find_elements_by_xpath(xpath_dict[key])
        text_value=[data.text for data in elements]
        datadict.update({key:text_value})
    driver.quit()
    return datadict

def makeurl(xpath_dict,url,baseurl):
    '''
        returns list
    '''
    data=scrape(xpath_dict,url)
    for key in data:
        urls=[ baseurl+keyword.replace(' ','+') for keyword in data[key] ]
    return urls



if __name__=='__main__':
    xpath_dict = {'cities':'//tbody//tr//td[1]'}
    url = 'http://worldpopulationreview.com/continents/cities-in-europe/'
    baseurl = 'https://angel.co/companies?keywords='
    data = makeurl(xpath_dict,url,baseurl)
    print(data)
    print(len(data))
    

