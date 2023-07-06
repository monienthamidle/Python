baseballteams = ['cardinals', 'rangers', 'red sox', 'tigers', 'astros', 'pirates', 'cubs' ]
#for baseballteam in baseballteams:
	#print(baseballteam)

#baseballteams = ['cardinals', 'rangers', 'red sox', 'tigers', 'astros', 'pirates', 'cubs' ]
#for baseballteam in baseballteams:
	#print(baseballteam.title())


#baseballteams = ['cardinals', 'rangers', 'red sox', 'tigers', 'astros', 'pirates', 'cubs' ]
#for baseballteam in baseballteams:
	#print(f"I Like the {baseballteam.title()} team.")


#baseballteams = ['astros', 'pirates', 'cubs' ]
#for baseballteam in baseballteams:
	#print(f"I Like the {baseballteam.title()} team.")
	#print(f'\tHow many World Series has the {baseballteam.title()} won.\n')
	#print()
	#print('-----------------End of Loop--------------')


# or 
# not in loop logic error 
for baseballteam in baseballteams:
	print(f'I Like the {baseballteam.title()} team.')
	print(f'How many World Series has the {baseballteam.title()} won.\n')

#not in loop
print('-----------------End of Loop--------------')

# or 
# error no statements in loop 
#for baseballteam in baseballteams:
	#print(f'I Like the {baseballteam.title()} team.')
	#print(f'How many World Series has the {baseballteam.title()} won.\n')
#print('-----------------End of Loop--------------')


#baseballteams = ['cardinals', 'rangers', 'red sox', 'tigers', 'astros', 'pirates', 'cubs' ]
#prints the first four 0-3 
#print(baseballteams[0:4])

#prints 3 & 4 
#print(baseballteams[2:4]) #red soxs and tigers

#prints 0-2 
#print(baseballteams[:3]) #less than 3 prints cardinals, rangers, red sox

#prints 3-6 (end)
#print(baseballteams[3:])

#prints 3-6 (end)
#print(baseballteams[-5])



# A new list is assigned 
#baseballteamsSet2 = baseballteams[:]
#baseballteamsSet2.append('Expos')
#baseballteamsSet2.append('white sox')
#print(baseballteams)
#print(baseballteamsSet2)



# list 
baseballteams = ['cardinals', 'rangers', 'red sox', 'tigers', 'astros', 'pirates', 'cubs']
#immutable - tulpe can not be change after receiving initial values
baseballteamstuple = ('cardinals', 'rangers', 'red sox', 'tigers', 'astros', 'pirates', 'cubs')
#list 
intValues = [5, 6, 4, 7, 0, 3, 8, 2, 9, 1]
#immutable - tulpe cannot be changed 
intValuestuple = (5, 6, 4, 7, 0, 3, 8, 2, 9, 1)
print(baseballteams)
print(baseballteamstuple)
print(intValues)
print(intValuestuple)

print(baseballteamstuple[0:3])


