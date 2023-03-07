import pprint
from decouple import config
import requests
import json
import tkinter as tk

RAPID_API_KEY = config('RAPID_API_KEY')

root = tk.Tk()
root.title('Heroes and Vilains Search API')
# create entry widget to get user input
search_entry = tk.Entry(root,font=('Times',12))
search_entry.pack(pady=10)

# print("Hello welcome to our heroes and villains search API :-)")
def search_heroes():
    url = "https://superhero-search.p.rapidapi.com/api/"

    # querystring = input("Which hero or villain would you like to search for?")
    querystring = search_entry.get()

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

    if response.status_code == 200:
        data = json.loads(response.text)
        result_text = pprint.pformat(data)
    else:
        result_text = f"Request failed with status code: {response.status_code}"


    result_label.config(text=result_text)
# create a button to initiate api request
search_button= tk.Button(
    root,
    text = "Search",
    font=('Times',12),
    command=search_heroes
    )
search_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=('TkDefaultFont', 12), wraplength=500)
result_label.pack(pady=10)



root.mainloop()
