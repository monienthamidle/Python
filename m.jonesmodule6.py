dogs = {'color': 'brown', 'eye color': 'black', 'gender': 'female', 'breed': 'jack russell', 'age': 15, 'size': 'small', 'hair': 'short', 'tail': 'long', 'nails': 'short', 'ears': 'pointy'}
print(dogs)
#print(f"\nPlease select a characteristic {dogs[value]}.")
print('---------------')

print('-----------------------')



for key, value in dogs.items():
	print(f"\nKey: {key} Value: {value}")
print()

print('---------------')


#for value in dogs.keys():
	#print(f"{value.title()}")
#print()


print('---------------')



for value in dogs.keys():

	if value == 'color':
		print(f"The color of my dog is {dogs[value]}.")

	elif value == 'eye color':
		print(f"The eye color of my dog is {dogs[value]}.")	
	elif value == 'gender':
		print(f"The gender of my dog is {dogs[value]}.")
	elif value == 'breed':
		print(f"The breed of my dog is {dogs[value]}.")
	elif value == 'age':
		print(f"The age of my dog is {dogs[value]}.")
	elif value == 'size':
		print(f"The size of my dog is {dogs[value]}.")
	elif value == 'hair':
		print(f"The hair on my dog is {dogs[value]}.")
	elif value == 'tail':
		print(f"The tail on my dog is {dogs[value]}.")
	elif value == 'nails':
		print(f"The nails on my dog are {dogs[value]}.")
	elif value == 'ears':
		print(f"The ears on my dog are {dogs[value]}.")
	else:
		print('No value found.')	
print('---------------------------------')			
#print(f"Please select one {dogs['color']}.")
#print(f"\nPlease select one characterstic or feature of a dog you like to have.")
#print(dogs["breed"])

for dog in dogs:
	print(dog)
dog = input("\nEnter a dog characteristic: \n")
print(f"\nCharacteristic {dogs}")
print(dogs[dog])
