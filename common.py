import requests
from collections import Counter
import requests
import datetime

def fetch_crime_stats_for_postcode(postcode):
    url = "https://api.postcodes.io/postcodes/" + postcode
    #ignore warning
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        latitude = str(response.json()["result"]["latitude"])
        longitude = str(response.json()["result"]["longitude"])
        admin_ward = str(response.json()["result"]["admin_ward"])
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None, None

    poly = str(float(latitude) + 0.0045) + "," + str(float(longitude) + 0.0045) + ":" + str(float(latitude) + 0.0045) + "," + str(float(longitude) - 0.0045) + ":" + str(float(latitude) - 0.0045) + "," + str(float(longitude) - 0.0045) + ":" + str(float(latitude) - 0.0045) + "," + str(float(longitude) + 0.0045)
    url = "https://data.police.uk/api/crimes-street/all-crime?poly=" + poly

    #get current month and year
    now = datetime.datetime.now()
    #urls should be last 12 months
    #construct &date first
    dates = [
        str(now.year) + "-" + str(now.month - i - 2) for i in range(now.month-3)#go back 2 months
    ]
    #now get remaining months from last year
    dates.extend([
        str(now.year - 1) + "-" + str(12 - i) for i in range(12 - now.month + 2)
    ])

    urls = [
        url + "&date=" + date for date in dates
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

    return stats, (latitude, longitude), admin_ward