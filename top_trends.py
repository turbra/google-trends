import sys
import requests
import pycountry
import json

def get_top_trends(country):
    url = f"https://trends.google.com/trends/api/dailytrends?hl=en-US&tz=-240&geo={country}&ns=15"
    response = requests.get(url)

    response_data = response.text[5:]
    data = json.loads(response_data)["default"]["trendingSearchesDays"][0]["trendingSearches"]

    top_3_trends = [entry["title"]["query"] for entry in data[:3]]

    return ", ".join(top_3_trends)

def is_valid_country_code(country_code):
    try:
        pycountry.countries.lookup(country_code)
        return True
    except LookupError:
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a country as a command-line argument.")
    else:
        country = sys.argv[1]
        if is_valid_country_code(country):
            trends = get_top_trends(country)
            print(trends)
        else:
            print(f"Invalid country code: {country}. Please provide a valid 2-letter ISO 3166-1 alpha-2 country code.")
