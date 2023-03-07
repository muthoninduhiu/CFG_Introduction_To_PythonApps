import pprint
import requests
import json
import tkinter as tk
from tkinter import messagebox
from decouple import config

RAPID_API_KEY = config('RAPID_API_KEY')

root = tk.Tk()
root.title('Heroes and Villains Search API')

frame = tk.Frame(root)
frame.pack()

entry_label = tk.Label(frame, text="Enter the name of hero or villain:")
entry_label.grid(row=0, column=0)

hero_entry = tk.Entry(frame)
hero_entry.grid(row=0, column=1)

url = "https://superhero-search.p.rapidapi.com/api/"
headers = {
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": "superhero-search.p.rapidapi.com"
}

def get_hero_details():
    querystring = hero_entry.get()
    response = requests.request("GET", url, headers=headers, params={'hero': querystring})
    if response.status_code == 200:
        data = json.loads(response.text)
        result_text = pprint.pformat(data)
        tk.messagebox.showinfo("Search Results", result_text)
    else:
        tk.messagebox.showerror("Error", f"Request failed with status code: {response.status_code}")

search_button = tk.Button(frame, text="Search", command=get_hero_details)
search_button.grid(row=1, column=1)

root.mainloop()
