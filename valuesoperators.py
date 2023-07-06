value_01 = 77
value_02 = 77
value_03 = 78
value_04 = 78

#if value_01 != value_02:
	#print('value_01 != value_03 True #1')

#if value_01 != value_03:
	#print('value_01 != value_03 True #2')

#if value_02 == value_03:
	#print('value_02 == value_03 True #3')

#print()


#if value_01 == (value_02 - 1):
	#print('value_01 == value_02 - 1 True #4')

#if (value_01 + 1) == value_02:
	#print('value_01 + 1 == value_02 True #5')

#and operator 
#will print
if value_01 == value_02 and value_03 == value_04:
	print('value_01 == value_02 and value_03 == value_04 - true #1')

#willnot print
if value_01 == value_02 and value_02 == value_03:
	print('value_01 == value_02 and value_02 == value_03 - true #2')	

#will print
if value_01 + 1 == value_03 and value_02 + 1 == value_04:
	print('value_01 + 1 == value_03 and value_02 + 1 == value_04 - true #3')	

#will print 
if value_01 == value_03 - 1 and value_02 == value_04 - 1:
	print('value_01 == value_03 - 1 and value_02 == value_04 - 1 - true #3')		



#or operators 
#will print
if value_01 == value_02 or value_03 == value_04:
	print('value_01 == value_02 or value_03 == value_04 - true #1')

	#will print
if value_01 == value_02 or value_02 == value_03:
	print('value_01 == value_02 or value_02 == value_03 - true #2')	


#will print
if value_01 == value_02 or value_01 == value_04:
	print('value_01 == value_02 or value_01 == value_04 - true #3')		

#willnot print
if value_01 == value_04 or value_02 == value_04:
	print('value_01 == value_04 or value_02 == value_04 - true #4')		