import pprint
from decouple import config
import requests

RAPID_API_KEY = config('RAPID_API_KEY')

print("Hello welcome to our heroes and villains search API :-)")

url = "https://superhero-search.p.rapidapi.com/api/"

# querystring = {"hero": "darth vader"}
querystring = input("Which hero or villain would you like to search for?")

headers = {
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": "superhero-search.p.rapidapi.com"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    params=
    {
        'hero':  querystring
    }
)

pprint.pprint(response.text)
