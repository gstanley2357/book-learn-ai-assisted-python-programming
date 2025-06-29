"""
open the csv file called "nfl_offensive_stats.csv" and read in the
csv data from the file
"""
"""
import csv
with open('nfl_offensive_stats.csv', 'r') as f:
    reader = csv.reader(f)
    nfl_data = list(reader)
"""
"""
In the data we just read in, the fourth column is the player
and the 8th column is the passing yards. Get the sum of
yards from column 8 where the 4th column value is
"Aaron Rodgers"
"""
"""
passing_yards = 0
for row in nfl_data:
    if row[3] == 'Aaron Rodgers':
        passing_yards += int(row[7])
print(passing_yards)
"""

"""
open the csv file called "nfl_offensive_stats.csv" and read
in the csv data from the file
"""

# import the csv module
import csv

# open the csv file
with open('nfl_offensive_stats.csv', 'r') as f:
    # read the csv data
    data = list(csv.reader(f))
"""
the 3rd column is player position, the 4th column is
the player, and the 8th column is the passing yards.
For each player whose position in column 3 is "QB",
determine the sum of yards from column 8
"""
# create a dictionary to hold the player name and passing yards
passing_yards = {}

# loop through the data
for row in data:
    # check if the player is a quarterback
    if row[2] == 'QB':
        # check if the player is already in the dictionary
        if row[3] in passing_yards:
            # add the passing yards to the existing value
            passing_yards[row[3]] += int(row[7])
        else:
            # add the player to the dictionary
            passing_yards[row[3]] = int(row[7])
"""
print the sum of the passing yards sorted by sum
of passing yards in descending order
"""
"""
for player in sorted(passing_yards, key=passing_yards.get, reverse=True):
    print(player, passing_yards[player])
"""

"""
print the sum of the passing yards sorted by sum
of passing yards in descending order
Do not include Tom Brady because he wins too much
"""
for player in sorted(passing_yards, key=passing_yards.get, reverse=True):
    if player != 'Tom Brady':
        print(player, passing_yards[player])

"""
plot the players by their number of passing yards only for
players with more than 4000 passing yards
"""
import matplotlib.pyplot as plt
import numpy as np
# create a list of players
players = []
# create a list of passing yards
yards = []
# for each player in the dictionary
for player in passing_yards:
    # if the player has more than 4000 passing yards
    if passing_yards[player] > 4000:
        # add the player to the list of players
        players.append(player)
        # add the passing yards to the list of passing yards
        yards.append(passing_yards[player])

# create a numpy array of the passing yards
yards = np.array(yards)
# create a numpy array of the players
players = np.array(players)
# sort the players by the passing yards
print(np.argsort(yards))
players = players[np.argsort(yards)]
# sort the passing yards
yards = np.sort(yards)
# create a figure
plt.figure()
# create a bar chart of the players and their passing yards
plt.bar(players, yards)
# rotate the x-axis labels
plt.xticks(rotation=90)
# show the plot
plt.show()
