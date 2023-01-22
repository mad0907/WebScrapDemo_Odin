from requests_html import HTMLSession
from bs4 import BeautifulSoup


s = HTMLSession()

url = 'https://www.amazon.in/s?k=dslr+camera+republic+day+sale&crid=GPG241DHGXVM&sprefix=dslr+camera+republic+day+sale%2Caps%2C187&ref=nb_sb_noss'

def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getnextpage(soup):
    # this will return the next page URL
    pages = soup.find('span', {'class': 's-pagination-strip'})
    if not pages.find('span', {'class': 's-pagination-item s-pagination-previous s-pagination-disabled '}):
        url = 'https://www.amazon.co.in' + str(pages.find('span', {'class': 's-pagination-item s-pagination-button'}).find('a')['href'])
        return url
    else:
        return


while True:
    data = getdata(url)
    url = getnextpage(data)
    if not url:
        break
    print(url)