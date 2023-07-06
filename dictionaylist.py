#check if item is in another list 

WorldSeries = {
2006: 'Cardinals',
2007: 'Red Sox',
2008: 'Phillies',
2009: 'Yankees',
2010: 'Giants',
2011: 'Cardinals',
2012: 'Giants',
2013: 'Red Sox',
2014: 'Giants',
2015: 'Royals',
2016: 'Cubs',
2017: 'Astros',
2018: 'Red Sox',
2019: 'Nationals',
}


lastThreeWins = [
'Astros',
'Red Sox',
'Nationals'
]

FavoriteTeams = [
'Cardinals',
'Yankees'
]

print('-----------------------')
print('Last Three Wins Test')
print()


print('------------------')
print('------------------')
print('Original Order')



for year in WorldSeries.keys():
	print(f"THe year played is {year}, the winning team was the {WorldSeries[year]}.")
	
	if WorldSeries[year] in lastThreeWins:
		print (f"\t\tThe {WorldSeries[year]} team is in the lastThreeWins List.")


print('------------------')
print('------------------')
print('Sorted Order')
print('------------------')



for year in sorted(WorldSeries.keys()):
	print(f"THe year played is {year}, the winning team was the {WorldSeries[year]}.")
	
	if WorldSeries[year] in lastThreeWins:
		print (f"\t\tThe {WorldSeries[year]} team is in the lastThreeWins List.")


print('------------------')
print('------------------')
print('Sorted Order - Uppercase')
print('------------------')


for year in sorted(WorldSeries.keys()):
	print(f"THe year played is {year}, the winning team was the {WorldSeries[year].upper()}.")
	
	if WorldSeries[year] in lastThreeWins:
		print (f"\t\tThe {WorldSeries[year].upper()} team is in the lastThreeWins List team.")
