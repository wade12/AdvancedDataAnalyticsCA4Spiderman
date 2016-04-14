## imports
import requests
from bs4 import BeautifulSoup

## define function
def spider(maxPages):
    page = 1
    while page <= maxPages:
        ## set url to crawl
        url = 'http://www.myhome.ie/residential/donegal/property-for-sale-in-quigleys-point'
        ## connect to website and request data from website
        ## store results in a variable called sourceCode
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        ## need to convert to a beautifulSoup object
        soup = BeautifulSoup(plainText, 'html.parser')
        ## loop through source code and pick out links with a class of ResidentialForSale
        for link in soup.findAll('a', {'class': 'ResidentialForSale'}):
            ## now select out the text inside the href attribute
            href = 'http://www.myhome.ie/residential/donegal/property-for-sale-in-quigleys-point' + link.get('href')
            address = link.string
            print(address)
        page += 1

## function call        
spider(1)
