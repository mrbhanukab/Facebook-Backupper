from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

with open("logo.txt", "r") as f:
    logo = f.read()
print(logo)

options = Options()
options.add_argument("user-data-dir=C:/Users/mrbha/AppData/Local/Google/Chrome/User Data")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

s = Service("D:\Projects\Facebook Backupper\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

# set the URL of the Facebook page
target_url = "https://www.facebook.com/people/Test-page/100091771551742/?sk=photos_albums"

# navigate to the target URL
driver.get(target_url)

# wait for the page to load
time.sleep(6)

# get the page source
resp = driver.page_source

# create a BeautifulSoup object
soup = BeautifulSoup(resp, 'html.parser')

# find the first 3 album links
album_links = [a['href'] for a in soup.find_all('a', {'class': 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv'}) if '/media/set/?set=a.' in a['href']][:3]
print(len(album_links))
print(album_links)
# loop through the album links and extract the image links from each album
for album_link in album_links:
    print("Images :"+ album_link)
    # navigate to the album link
    driver.get(album_link)
    # wait for the page to load
    time.sleep(6)
    # get the page source
    resp = driver.page_source
    # create a BeautifulSoup object
    soup = BeautifulSoup(resp, 'html.parser')
    # find all image links in the album
    image_links = [a['href'] for a in soup.find_all('a', {'class': 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv'})]
    # print the image links
    print(image_links)

# close the driver
driver.close()