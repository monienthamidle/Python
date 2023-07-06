#Dictionary key value pairs
#Three key-value pairs winningTeam, year, losingTeam 



FirstWorldSeries = {'winningTeam': 'Red Sox', 'year': '1903', 'losingTeam': 'Pirates'}
print('----------------------------')
print(f"The first world series results were {FirstWorldSeries}.")
print('----------------------------')
print(f"The first team to win a World Seriew was the {FirstWorldSeries['winningTeam']}.")#displays a particular elements information
print(f"The first World Series was played in {FirstWorldSeries['year']}.")
print(f"The first team to lose a World Serices was the {FirstWorldSeries['losingTeam']}.")
print()

FirstWorldSeries['winningCity'] = 'Boston'
FirstWorldSeries['losingCity'] = 'Pittsburgh'
print('----------------------------')
print(f"The first world series results were {FirstWorldSeries}.")
print('----------------------')
print()
print(f"The home of the first World Series winner was {FirstWorldSeries['winningCity']}.")
print(f"The home of the first World Series loser was {FirstWorldSeries['losingCity']}.")
print()


#if condition test 
FirstWorldSeries = {'winningTeam': 'Red Sox', 'year': '1903', 'losingTeam': 'Pirates'}
FirstWorldSeries['winningCity'] = 'Boston'
FirstWorldSeries['losingCity'] = 'Pittsburgh'

if FirstWorldSeries['winningCity'] == 'St. Louis':
	print('The winning city was St. Louis')
elif FirstWorldSeries['winningCity'] == 'Boston':
	print(f"The home of the first World Series winner was {FirstWorldSeries['winningCity']}.")
else:
	print("We are not sure of the winning location.")
