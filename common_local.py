# Description: This file contains the common functions that are only used locally.
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

def fetch_postcode_from_zoopla(url):
    try:
        # Create a new instance of the Chrome driver
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")

        # Create a new instance of the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to the provided URL
        driver.get(url)

        # Use beautiful soup to parse the html
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find type="application/json"
        element = soup.find('script', type="application/json")

        # Extract and return the outcode and incode
        outcode = element.text.split('"outcode":"')[1].split('"')[0]
        incode = element.text.split('"incode":"')[1].split('"')[0]

        # Close the browser
        driver.quit()
        print("Postcode from Zoopla: " + outcode + " " + incode)

        return outcode + " " + incode
    except Exception as e:
        # Handle exceptions gracefully
        print(f"Chrome Driver: An error occurred: {e}")
        driver.quit()
        return None
