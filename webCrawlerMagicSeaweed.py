import requests
from bs4 import BeautifulSoup

def spider():
    ## set url to crawl
    url = 'http://magicseaweed.com/Dunfanaghy-Surf-Report/1100/'
    ## connect to website and request data from website
    ## store results in a variable called sourceCode
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    ## need to convert to a beautifulSoup object
    soup = BeautifulSoup(plainText, 'html.parser')
    ## loop through source code and pick out links with a class of ResidentialForSale
    #for link in soup.findAll('a', {'class': 'details-link to-fpa'}):
    for link in soup.findAll('a', {'class': 'ResidentialForSale'}):
        ## now select out the text inside the href attribute
        #href = link.get('url')
        href = 'http://www.myhome.ie/residential/dublin-county/house-for-sale-in-blackrock-dublin?page=' + link.get('href')
        #title = link.string
        address = link.string
        #print(href)
        #print(title)
        print(address)
        ## call single car data function
        #getSingleCarData(href)
                   
spider()


