from common import fetch_crime_stats_for_postcode
from common_local import fetch_postcode_from_zoopla
from common import visualize_crime_stats

def run_cli_local(input_data):
    postcode_input = input_data
    #postcode_input = input("Enter postcode or Zoopla URL: ")

    if "zoopla.co.uk" in postcode_input:
        postcode = fetch_postcode_from_zoopla(postcode_input)
        if not postcode:
            print("Failed to retrieve postcode from the URL.")
            return
    else:
        postcode = postcode_input

    stats, lat_lon, admin_ward = fetch_crime_stats_for_postcode(postcode)
    if stats and lat_lon and admin_ward:
        print("The location is:", admin_ward)
        print("In the last 12 months, there are", stats["crime_count"], "crimes in the area.")
        print("The most frequent crimes are", stats["top_three_frequent_crime"])
        print("The most frequent street is", stats["most_frequent_street"])
        print("The number of crimes in the last 12 months are:")
        print(stats["monthly_crime_count"])
    else:
        print("Unable to fetch data.")
    visualize_crime_stats(stats, postcode)


if __name__ == "__main__":
    run_cli_local()
