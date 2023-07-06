
#i = 0

#while i <= 20:
	#print(f'{i}')
	#i += 1

#following not allowed in python
	#error 
	# ++ i
	#error
	#i++
#use while loop when you are not sure of the interations



#sentinel value

#inputMessage = input('Enter a message to be displayed: ')

#while inputMessage.lower() != 'quit':
	#print(f'You entered {inputMessage}.')
	#inputMessage = input('Enter a message to be displayed: ')

#print('The program will now quit.')


sentinelValue = '999'
total = 0 

inputValue = input('Enter an int value to be added to the total, 999 to quit: ')

while inputValue != sentinelValue:
	total += int(inputValue)
	print(f'The total is now {total}.')
	inputValue = input('Enter an int value to be added to the total, 999 to quit: ')

print(f'The final total was {total}.')
print('The program will end.')
