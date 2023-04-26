# Facebook Album Downloader

This Python script uses Selenium and BeautifulSoup to download Facebook albums. 

## Prerequisites

- Python 3.x
- Required libraries: `os`, `time`, `json`, `requests`, `bs4`, `selenium`, `tqdm`
- Chrome Browser
- `chromedriver.exe` (download the driver for your Chrome version from [here](https://chromedriver.chromium.org/downloads))

## How to use

1. Clone the repository and navigate to the project directory.
2. Install the required libraries: `pip install -r requirements.txt`
3. Download and install the `chromedriver.exe` and save it in the project directory.
4. Run the script: `python album_downloader.py`
5. The script will prompt you to log in to Facebook.
6. After login, the script will automatically download all the albums from the Facebook page specified in the `target_url` variable in the script.

The script will prompt you to log in to Facebook. After logging in, it will download the images from the albums on the Facebook page specified in the target_url variable. By default, the first two albums found on the page will be downloaded. You can change this by modifying the album_links variable.

The downloaded images will be saved in a directory named `albums` in the same directory as the script. The metadata for each album will be saved in a `metadata.json` file in the album directory.

**Note 1:** The script is set up to exclude certain album links (specified in the ``exclude_album_links` variable) to avoid downloading duplicate albums. You can modify this list to exclude additional albums if necessary.

**Note 2:** The script is set up to wait for 30 seconds after navigating to each album link to allow for the images to load. You can modify this time by changing the `time.sleep(30)` line in the script.

**Note 3:** The script is set up to use the Chrome WebDriver. If you are using a different browser, you will need to modify the script accordingly.

### **File Structure**
albums/ <br />
├── Album 1/ <br />
│   ├── photo1.jpg <br />
│   ├── photo2.jpg <br />
│   └── metadata.json <br />
├── Album 2/ <br />
│   ├── photo1.jpg <br />
│   ├── photo2.jpg <br />
│   └── metadata.json <br />
|── Album 3/ <br />
|  ├── photo1.jpg <br />
|   ├── photo2.jpg <br />
|   └── metadata.json <br />
| <br />

## Disclaimer

This script is for educational and personal use only. Please respect the privacy and copyright of the owners of the albums you download using this script.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

This script was created by [MrBhanuka](https://github.com/mrbhanukab).

[![website](https://img.shields.io/badge/Github%20Page-mrbhanukab.github.io-lightgrey?style=for-the-badge&logo=GitHubr&logoColor=white)](https://mrbhanukab.github.io/) <br>
[![github](https://img.shields.io/badge/Github-mrbhanukab-%23333?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/mrbhanukab) <br>
[![twitter](https://img.shields.io/badge/Twitter-mrbhanuka-%2300acee?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/mrbhanuka)

**Note: Please make sure to replace folder_path in the README.md file with the actual path to your music folder.**
