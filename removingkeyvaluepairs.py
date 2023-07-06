#removing key-value pairs 

FirstWorldSeries = {'winningTeam': 'Red Sox', 'winningCity': 'Boston', 'year': '1903', 'losingTeam': 'Pirates', 'losingCity': 'Pittsburgh'}
print('----------------------')
print(f"The first world series results were {FirstWorldSeries}.")
print('----------------------')

print(f"The home of the first World Series winner was {FirstWorldSeries['winningCity']}.")
print(f"The home of the first World Series loser was {FirstWorldSeries['losingCity']}.")

del FirstWorldSeries['winningCity']

del FirstWorldSeries['losingCity']

print('-----------------------')
print(f"The first world series results were {FirstWorldSeries}.")


print('-----------------------')
resultMessage = FirstWorldSeries.get('winningCity', 'Sorry, the winning city was not found.')
print(resultMessage)
print('-----------------------')
resultMessage = FirstWorldSeries.get('losingCity', 'Sorry, the losing city was not found.')
print(resultMessage)
print('-----------------------')


states = {
    'St. Louis': 'Cardinals',
    'Chicago': 'Cubs',
    'New York': 'Yankees',
    'Boston': 'Red Sox',
}

for state in states:
    print(state)

state = input(
    "\nEnter a state\n")

print("\n")
print(states[state])