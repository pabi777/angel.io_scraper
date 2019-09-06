import csv
import requests
import os

class Scraper:
    def read(self):
        try:
            with open('companies.csv','r') as csvfile:
                reader=csv.reader(csvfile,delimiter=',')
                data=[line for line in reader]
                company_names=[data[0].split('\n')[0] for data in data]
                websites=[data[1] for data in data]
                compdict=dict(zip(company_names,websites))
            print(compdict)
            return compdict
        except Exception as e:
            print(e)
        
    def download_page(self):
        companies = self.read()
        
        # define the name of the directory to be created
        path = "company"
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
        for company in companies:
            try:
                req=requests.get('https://'+companies[company])
                with open('company/'+company+'.html','w') as htmlfile:
                    htmlfile.write(req.text)
            except:
                
                with open('retry.txt','a') as retry:
                    retry.write('https://'+companies[company]) 
                print('https://'+companies[company])
            
            





    

Scraper().download_page()


            