
#below gives an error in CMD due to integer 

#userInput = input('Enter a number between 0 and 11: ')

#print(f'The value entered was {userInput}')

#if userInput > 0 and userInput < 11:
	#print('The value of {userInput} is correct.')



#correct way converting number into integer 

#userInput = input('Enter a number between 0 and 11: ')

#print(f'The value entered was {userInput}')

#userInputInt = int(userInput)

#if userInputInt > 0 and userInputInt < 11:
	#print(f'The value of {userInput} is correct.')
#else:
	#print(f'The value of {userInput} is incorrect.')



userInput = input('Enter an integer value: ')

userInputInt = int(userInput)

if userInputInt % 2 == 0:
	print(f'The input value of {userInputInt} is even.')
else:
	print(f'The input value of {userInputInt} is odd.')

