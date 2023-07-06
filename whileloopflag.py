#flag

active = True 
displayString = ''

while active:

	inputMessage = input('Enter letter(s) to be added together, enter \'exit\' to quit: ')

	if inputMessage.lower() == 'exit':
		print(f'The letters in put were "{displayString}".')
		active = False
	else:
		displayString += inputMessage

print
