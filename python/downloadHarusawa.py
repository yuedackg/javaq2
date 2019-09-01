#
from urllib import request
from bs4 import BeautifulSoup

def scraping():
    #url 
    url = "http://eromanga-marugoto.com/book_title/彼女が堕ちるまで"
    print (url)
    # get html 
    html = request.urlopen( url)

    #set beautifulsoup
    soup = BeautifulSoup( html, "html.parser")
    #get headlines
    mainNewsIndex = soup.find( "ul", attrs={"class", "list-main-news"})
    print ( mainNewsIndex)


scraping()

test  = "hello"
print( test)
