# Create a dictionary that will accept cricket players name and
# scores in a match. Also we are retrieving runs by entering the
# player’s name

# Create an empty dictionary
cricket_scores = {}

# Take input for number of players
n = int(input("Enter number of players: "))

# Accept players' names and scores
for i in range(n):
    name = input(f"Enter player {i+1} name: ")
    runs = int(input(f"Enter {name}'s runs: "))
    cricket_scores[name] = runs

print("\nAll players and scores:", cricket_scores)

# Retrieve runs by player name
search_name = input("\nEnter player name to get runs: ")

if search_name in cricket_scores:
    print(f"{search_name} scored {cricket_scores[search_name]} runs.")
else:
    print(f"No data available for {search_name}.")


# Additionally, find players with a specific score
search_score = int(input("\nEnter score to find players with that score: "))

players_with_score = []
for name, score in cricket_scores.items():
    if score == search_score:
        players_with_score.append(name)

if players_with_score:
    print(f"Players with {search_score} runs: {', '.join(players_with_score)}")
else:
    print(f"No players found with {search_score} runs.")
