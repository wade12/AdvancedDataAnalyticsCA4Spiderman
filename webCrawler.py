import requests
from bs4 import BeautifulSoup

def spider(maxPages):
    page = 1
    while page <= maxPages:
        ## set url to crawl
        #url = 'http://www.carzone.ie/search/result/cars/make/porsche/model/cayman'
        #url = 'http://www.myhome.ie/residential/dublin-county/house-for-sale-in-blackrock-dublin'
        url = 'http://www.myhome.ie/residential/donegal/property-for-sale-in-quigleys-point'
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
            #href = 'http://www.carzone.ie' + link.get('href')
            #href = 'http://www.myhome.ie' + link.get('href')
            #href = 'http://www.myhome.ie/residential/dublin-county/house-for-sale-in-blackrock-dublin'
            #href = 'http://www.myhome.ie/residential/dublin-county/house-for-sale-in-blackrock-dublin?page=' + link.get('href')
            href = 'http://www.myhome.ie/residential/donegal/property-for-sale-in-quigleys-point'
            #title = link.string
            address = link.string
            #print(href)
            #print(title)
            print(address)
            ## call single car data function
            #getSingleCarData(href)
        page += 1

# def getSingleCarData(carUrl):
        # sourceCode = requests.get(url)
        # plainText = sourceCode.text
        # ## now convert to a new beautifulSoup object
        # soup = BeautifulSoup(plainText, 'html.parser')
        # ## now crawl it, pull out links, titles, etc.
        # for carName in soup.findAll('div', {'class': 'i-name'}):
            # print(carName.string)
                   
spider(1)

