#while True 


#total = 0 

#inputValue = input('Enter an int value to be added to the total, 999 to quit: ')

#while True: 
	#if inputValue == '999':
		#break


	#total += int(inputValue)
	#print(f'The total is now {total}.')
	#inputValue = input('Enter an int value to be added to the total, 999 to quit: ')

#print(f'The final total was {total}.')
#print('The program will end.')


#while True 
#only add the even numbers 

total = 0 



while True: 
	inputValue = int(input('Enter an int value to be added to the total, 999 to quit: '))


	if inputValue == 999:
		break
	elif inputValue % 2 == 1:
		continue
	else:
		total += int(inputValue)
		print(f'The total is now {total}.')
	

print(f'The final total was {total}.')
print('The program will end.')