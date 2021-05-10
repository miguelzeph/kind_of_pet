import os
from selenium import webdriver # Get the page_source
from bs4 import BeautifulSoup # to parse HTML
# para fazer o download
import urllib.request
import time


GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

# The User-Agent request header contains a characteristic string 
# that allows the network protocol peers to identify the application type, 
# operating system, and software version of the requesting software user agent.
# needed for google search
usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}


SAVE_FOLDER = 'images'

def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    download_images()
    
def download_images():
    
    browser = webdriver.Chrome('./driver_Chromium90/chromedriver') 
    
    # Os inputs
    data = input('What are you looking for? ')
    n_images = int(input('How many images do you want? '))

    print('Start searching...')
    print('\n')

    # get url query string
    searchurl = GOOGLE_IMAGE + 'q=' + data
    
    browser.get(searchurl)


    for y in range( 0 , 5 ):
        browser.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        time.sleep(0.5)

    soup = BeautifulSoup(browser.page_source) # Pulo do gato
    results = soup.findAll('img', {'class': 'rg_i Q4LuWd'}, limit=n_images)


    imagelinks= []
    #All the Src
    for result in results:
        imagelinks.append(result['src'])


    print(f'found {len(imagelinks)} images')
    print('Start downloading...')


    for i, imagelink in enumerate(imagelinks):

        imagelocal = f'./{SAVE_FOLDER}/{data}.{i}.jpg'
        urllib.request.urlretrieve( imagelink , imagelocal)

    print('Done')


if __name__ == '__main__':
    main()
