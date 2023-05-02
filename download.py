# Importing All Required Libraries
import os
import time
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By

# Call the clear_console function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def page_load(t):
    print("Wait for the page to load")
    for i in tqdm(range(100)):
        time.sleep(t/100)
clear_console()

# My Logo :)
with open("logo.txt", "r") as f:
    logo = f.read()
print(logo)
print("")

#URL of the Facebook page
target_url = "https://www.facebook.com/Ur_url_to_albums_page"

# set the directory to save images and metadata
dir_name = "albums"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
os.chdir(dir_name)
print(f"'{dir_name}' directory created and changed working directory to '{dir_name}'") 

# set up Selenium options and service
options = Options()
# options.add_argument("user-data-dir=C:/Users/{ur_username}/AppData/Local/Google/Chrome/User Data")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

s = Service("D:\Projects\Facebook Backupper\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

# navigate to the target URL
driver.get(target_url)
print("Navigated to the target URL")
# Scroll down the page to load all albums
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
# time.sleep(2)
    
# get the page source
resp = driver.page_source

# create a BeautifulSoup object
soup = BeautifulSoup(resp, 'html.parser')

# find the first n number of album links
album_links = [a['href'] for a in soup.find_all('a', {'class': 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv'}) if '/media/set/?set=a.' in a['href']][:6]
exclude_album_links = ["https://www.facebook.com/media/set/?set=a.125327670440598&type=3","https://www.facebook.com/media/set/?set=a.151326117840753&type=3", "https://www.facebook.com/media/set/?set=a.125327660440599&type=3", "https://www.facebook.com/media/set/?set=a.146707814969250&type=3"]  # list of album links to be excluded
album_links = [link for link in album_links if link not in exclude_album_links]
album_links.reverse()  # reverse the order of album_links in place

print("Total Number of Albums Found: " + str(len(album_links)))

o=0
for album_link in album_links:
    print(" ")
    print(" ")
    o = o + 1
    # navigate to the album link
    driver.get(album_link)
    print(f"Navigated to the URL, {album_link}")

    # print("Scroll to the bottom of the page by manualy, Im Waiting 30seconds")
    # time.sleep(30)

    # Scroll down the page to load all albums
    #! If This Not Working Comment down below and uncomment Above One
    last_height = driver.execute_script("return document.body.scrollHeight")
    print("I'm Scrolling Down")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    # get the page source
    resp = driver.page_source
    # create a BeautifulSoup object
    soup = BeautifulSoup(resp, 'html.parser')
    # get album name and description
    
    # create a dictionary for storing album metadata
    album_metadata = {"link": album_link}
    
    # create a directory for storing album images
    os.makedirs("Album "+str(o), exist_ok=True)
    os.chdir("Album "+str(o))
    with open('metadata.json', 'w') as f:
        json.dump(album_metadata, f)
    
    # find all image links in the album
    image_links = [a['href'] for a in soup.find_all('a', {'class': 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv'})]
    print(f"{str(len(image_links))} Images found in album {str(o)}")
    
    # download each image
    for i, link in enumerate(image_links): 
        print(f"Downloading image [{i+1}/{str(len(image_links))}]")
        # navigate to the image link
        driver.get("https://www.facebook.com" + link)
        # wait for the page to load
        time.sleep(0.5)
        # get the page source
        resp = driver.page_source
        # create a BeautifulSoup object
        soup = BeautifulSoup(resp, 'html.parser')
        # find the image source
        image = soup.find('img', {'data-visualcompletion': 'media-vc-image'})
        if image is not None:
            image_src = image.get('src')
            # download the image
            with open(f"image_{i+1}.jpg", 'wb') as f:
                response = requests.get(image_src)
                f.write(response.content)
        else:
            print(f"No image found")
            
    os.chdir("..")
# close the driver
driver.close()