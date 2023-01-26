import pprint

import requests

print("Hello welcome to our heroes and villains search API :-)")

url = "https://superhero-search.p.rapidapi.com/api/"

# querystring = {"hero": "darth vader"}
querystring = input("Which hero or villain would you like to search for?")

headers = {
    "X-RapidAPI-Key": "4f68a4da7bmsh4320fb69e248469p121f6djsn6ba74950580d",
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
