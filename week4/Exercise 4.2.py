"""
Make a list of game scores. Using list functions write code to output information of the
scores in the following format:

Extension: Output all of the scores in descending order
Number of scores: 10
Highest score: 200
Lowest score: 3
"""
game_scores = [
    10, 200, 55, 99, 6, 8, 3, 5, 6, 7
]

print("Number of scores: {}".format(len(game_scores)))
print("Highest Score: {}".format(max(game_scores)))
print("Lowest Score: {}".format(min(game_scores)))

sorted_scores = sorted(game_scores)
sort_descending = list(reversed(sorted_scores))
print(sorted_scores)
print(sort_descending)
