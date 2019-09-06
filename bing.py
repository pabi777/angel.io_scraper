# Import required modules.
from azure.cognitiveservices.search.websearch import WebSearchAPI
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials
from mysqlconn import MySQLConn

# Replace with your subscription key.
#subscription_key = "dddd533d73744ce1a885025602a8bbe5"

# Instantiate the client and replace with your endpoint.
#client = WebSearchAPI(CognitiveServicesCredentials(subscription_key), base_url = "https://api.cognitive.microsoft.com/bing/v7.0/")

# Make a request. Replace Yosemite if you'd like.

class BingSearch:
        def __init__(self):
            self.subscription_key = "dddd533d73744ce1a885025602a8bbe5"
            self.client = WebSearchAPI(CognitiveServicesCredentials(self.subscription_key), base_url = "https://api.cognitive.microsoft.com/bing/v7.0/")

        def query(self,string,no_of_results):
            try:
                no_of_results=int(no_of_results)
                web_data = self.client.web.search(query=string)
                '''
                Web pages
                If the search response contains web pages, the first result's name and url
                are printed.
                '''
                if hasattr(web_data.web_pages, 'value'):

                    #print("\r\nWebpage Results#{}".format(len(web_data.web_pages.value)))

                    first_web_page = web_data.web_pages.value[:no_of_results]
                    return([{data.name:data.url} for data in first_web_page ])
                    #print(first_web_page.url)
                    #print("First web page name: {} ".format(first_web_page.name))
                    #print("First web page URL: {} ".format(first_web_page.url))

                else:
                    print("Didn't find any web pages...")
            except Exception as e:
                print(e)

if __name__=='__main__':
    
    a=BingSearch().query('+"chief claims" site:linkedin.com/in/',1)
    print(a)

    with open('results.txt','a') as results:
        results.write(str(a))
    
    # for i in a:
    #     for v in i:
    #         print(i[v])
