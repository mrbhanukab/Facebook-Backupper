import os
import json
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


# Load the user data directory and create the Chrome driver with options
options = Options()
options.add_argument("user-data-dir=C:/Users/mrbha/AppData/Local/Google/Chrome/User Data")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

s = Service("D:\Projects\Facebook Backupper\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

# Set the URL of the Facebook page
target_url = "https://www.facebook.com/people/Test-page/100091771551742/?sk=photos_albums"

# Navigate to the target URL
driver.get(target_url)

# Wait for the page to load
time.sleep(6)

# Get the page source
resp = driver.page_source

# Create a BeautifulSoup object
soup = BeautifulSoup(resp, 'html.parser')

# Find all album links
album_links = [a['href'] for a in soup.find_all('a', {'class': 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv'}) if '/media/set/?set=a.' in a['href']]

# Loop through the album links and extract the image links from each album
for album_link in album_links:
    # Navigate to the album link
    driver.get(album_link)

    # Wait for the page to load
    time.sleep(6)

    # Get the page source
    resp = driver.page_source

    # Create a BeautifulSoup object
    soup = BeautifulSoup(resp, 'html.parser')

    # Find the album name from the span class
    album_name = soup.find('span', {'class': 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x14z4hjw x3x7a5m xngnso2 x1qb5hxa x1xlr1w8 xzsf02u x1yc453h'}).text.strip()

    # Create the folder with the album name if it doesn't exist
    folder_path = f"{album_name}_{album_link.split('=')[-1]}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create a dictionary to store the metadata
    metadata = {'album_name': album_name, 'image_links': []}

    # Find all image links in the album
    image_links = [a['href'] for a in soup.find_all('a', {'class': 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv'}) if '/photos/' in a['href']]

    # Loop through the image links and download the images
    for i, image_link in enumerate(image_links):
        # Navigate to the image link
        driver.get(f"https://www.facebook.com{image_link}")

        # Wait for the page to load
        time.sleep(6)

        # Get the page source
        resp = driver.page_source

        # Create a BeautifulSoup object
        soup = BeautifulSoup(resp, 'html.parser')

        # Find the image URL
        image_url = soup.find('img', {'class': 'x85a59c x193iq5w x4fas0m x19kjcj4'}).get('src')

        # Download the image and save it to the folder
        file_path = f"{folder_path}/{str(i).zfill(10)}.jpg"
        urllib.request.urlretrieve(image_url, file_path)

        # Add the image link to the metadata
        metadata['image_links'].append(image_link)

    # Save the metadata to a JSON file
    with open(f"{folder_path}/metadata.json", 'w') as f:
        json.dump(metadata, f)

# Close the driver
driver.close()
