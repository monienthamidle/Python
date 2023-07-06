cars_01 = ['car 1', 'car 2'] #List a dynamic sized arrarys
cars_02 = ('car 3', 'car 4') #Tuple list of items that cannot change 
cars_03 = {'car_5': 1, 'car_6': 2} #Dictionary key-value pairs

print(cars_01)
print(cars_02)
print(cars_03)

#Beyond our scope 
#One element with the final value of 2 
cars_04 = {'car_7': 1, 'car_7': 2}

#Two elements both with the value of 2
cars_05 = {'car_8': 2, 'car_9': 2}

print()
print('---------------------')

print(cars_04)
print('------------------')

print(cars_05)
print('-----------------------')
print()


#Looping through a dictionary

FirstWorldSeries = {'winningTeam': 'Red Sox', 'winningCity': 'Boston', 'year': '1903', 'losingTeam': 'Pirates', 'losingCity': 'Pittsburgh'}

#Use the dictonary items method 

for key, value in FirstWorldSeries.items():
	print(f"Key: {key} Value: {value}")
print()


#or

#for key, value in FirstWorldSeries.items():
	#if type(value) is int:
		#if int do not use upper () method
		#print(f"{key.title()} is {value}")
	#else: 
		#otherwise if not number user upper() method 
		#print(f"{key.title()} is {value.upper()}")




#Testing key value with if


FirstWorldSeries = {'winningTeam': 'Red Sox', 'winningCity': 'Boston', 'year': '1903', 'losingTeam': 'Pirates', 'losingCity': 'Pittsburgh'}

for value in FirstWorldSeries.keys():
	print(f"{value.title()}")

print()

#or 

for value in FirstWorldSeries.keys():

	if value == 'year':
		#note: here we did not use the firstworldseries['value'] string
		print(f"Year played was {FirstWorldSeries[value]}.")

	elif value == 'winningTeam':
		print(f"The first team to win a World Series was the {FirstWorldSeries[value]}.")	
	elif value == 'losingTeam':
		print(f"The first team to lose a World Series was the {FirstWorldSeries[value]}.")
	elif value == 'winningCity':
		print(f"The home of the first World Series winner was {FirstWorldSeries[value]}.")
	elif value == 'losingCity':
		print(f"The home of the first World Series loser was {FirstWorldSeries[value]}.")
	else:
		print('No value found.')		