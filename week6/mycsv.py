import csv

# Add code to open the csv file
with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    heights = []

    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)
