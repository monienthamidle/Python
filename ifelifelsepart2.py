baseballteams = ['cardinals', 'rangers', 'red sox', 'tigers', 'astros', 'pirates', 'cubs' ]
for baseballteam in baseballteams:
	if baseballteam != 'Rangers'.lower():
		print(f'{baseballteam.upper()} is the team we are looking for.(#1)')
	else:
		print(f'\t{baseballteam.title()} is not the correct team.')	

print ()
#This corrects the error 
for baseballteam in baseballteams:
	if baseballteam.title() == 'Rangers':
		print(f'\t{baseballteam.upper()} is the team we were looking for.')
	else:
		print(f'{baseballteam.title()} is not the correct team.')
print ()

#Depending the list data. maybe 
for baseballteam in baseballteams:
	if baseballteam.title() == 'rangers'.title():
		print(f'\t{baseballteam.upper()} is the team we were looking for.')
	else:
		print(f'{baseballteam.title()} is not the correct team.')
print()
print(baseballteams)


#team = 'Cardinals'		
#if team == 'Cardinals':
	#print('True - Cardinals #1')

#team = 'Cubs'
#if team == 'Cubs':	
	#print('True - Cubs #2')
#if team == 'Cardinals':
	#print('True - Cardinals #3')
#if team == 'cubs'.title():	
	#print('True - cubs #4')