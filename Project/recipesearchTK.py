import tkinter as tk
from tkinter import ttk
import requests
from decouple import config

# Your Edamam API credentials
APP_ID = config('APP_ID')
APP_KEY = config('APP_KEY')


def recipe_search(search_term):
    """
    Search for recipes from the web via an API.
    :param search_term: string - input chosen by user for a recipe.
    :return: a list of recipe(s) that match the search term by user.
    """
    # Make a request to the Edamam API with the required ingredient as part of the search query
    url = requests.get('https://api.edamam.com/api/recipes/v2',
                       headers={'Accept': 'application/json'},
                       params={
                           'app_id': APP_ID,
                           'app_key': APP_KEY,
                           'q': search_term,
                       })

    data = url.json()
    return data['hits']


def search_recipes():
    search_term = search_term_entry.get()
    results = recipe_search(search_term)
    for hit in results:
        recipe = hit['recipe']
        recipe_name = recipe['label']
        recipe_type = recipe['healthLabels']
        results_tree.insert("", tk.END, text=recipe_name, values=(recipe_type))


root = tk.Tk()
root.title("Recipe Search")
root.geometry("500x500")

# Add a label for the search term
search_term_label = tk.Label(root, text="Search Term:")
search_term_label.grid(row=0, column=0, padx=10, pady=10)

# Add an entry widget for the search term
search_term_entry = tk.Entry(root)
search_term_entry.grid(row=0, column=1, padx=10, pady=10)

# Add a search button
search_button = tk.Button(root, text="Search", command=search_recipes)
search_button.grid(row=0, column=2, padx=10, pady=10)

# Add a label to show the results
results_label = tk.Label(root, text="Results:")
results_label.grid(row=1, column=0, padx=10, pady=10)

# Add a treeview widget to show the results
results_tree = ttk.Treeview(root)
results_tree.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# Add column headers to the treeview widget
results_tree["columns"] = ("Type")
results_tree.column("Type", width=200, anchor="w")
results_tree.heading("Type", text="Type")

root.mainloop()
