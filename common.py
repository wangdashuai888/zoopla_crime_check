import requests
from collections import Counter
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def fetch_crime_stats_for_postcode(postcode):
    url = "https://api.postcodes.io/postcodes/" + postcode
    #ignore warning
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        latitude = str(response.json()["result"]["latitude"])
        longitude = str(response.json()["result"]["longitude"])
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None, None

    poly = str(float(latitude) + 0.0045) + "," + str(float(longitude) + 0.0045) + ":" + str(float(latitude) + 0.0045) + "," + str(float(longitude) - 0.0045) + ":" + str(float(latitude) - 0.0045) + "," + str(float(longitude) - 0.0045) + ":" + str(float(latitude) - 0.0045) + "," + str(float(longitude) + 0.0045)
    url = "https://data.police.uk/api/crimes-street/all-crime?poly=" + poly

    urls = [
        url + "&date=2023-06",
        url + "&date=2023-05",
        url + "&date=2023-04",
        url + "&date=2023-03",
        url + "&date=2023-02",
        url + "&date=2023-01",
        url + "&date=2022-12",
        url + "&date=2022-11",
        url + "&date=2022-10",
        url + "&date=2022-09",
        url + "&date=2022-08",
        url + "&date=2022-07",
    ]

    merged_results = []
    number_list = []

    for url in urls:
        #ignore warning
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            number_list.append(len(response.json()))
            merged_results.extend(response.json())
        else:
            print(f"Error {response.status_code}: {response.text}")

    outcome = merged_results
    category_list = [item["category"] for item in outcome]
    street_list = [item["location"]["street"]["name"] for item in outcome]

    stats = {
        "crime_count": len(outcome),
        "top_three_frequent_crime": Counter(category_list).most_common(3),
        "most_frequent_street": Counter(street_list).most_common(2)[1],#choosing the second most because the first most is "On or Near"
        "monthly_crime_count": number_list,
    }

    return stats, (latitude, longitude)

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

        #wait until the element is loaded
        wait = WebDriverWait(driver, 5)

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
