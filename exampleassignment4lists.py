# prints values of 1 to 5 (n - 1) 
for intValue in range(1,6):
	print(intValue)

# Error cannot use floating-point values
# for intValue in range (1.5, 6.5):
# print(intValue)

intValuesList = list(range(1, 5))
print(intValuesList)

multiplesofThreeList = list(range(3, 22, 3)) #prints 3, 3 - 21 (n - 1)
print(multiplesofThreeList)

multiplesofFourList = list(range(4, 29, 4)) #prints 4, 4 - 28 (n - 1)
print(multiplesofFourList)


cubesList = []
for cube in range(1,9):
	cubesList.append(cube * cube * cube)
print(cubesList)

squareList = []

for square in range(2, 20, 2):
	squareList.append(square * square)
print(squareList)	


intValuesList = [5, 6, 7, 0, 4, 3, 8, 9, 2, 1]
print(min(intValuesList))
print(max(intValuesList))
print(sum(intValuesList))

#Average 
print(f"The average is: {sum(intValuesList)/len(intValuesList)}")


floatValuesList = [2.5, 7.8, 9.5, 4.2, 1.1, 2.4, 6.8, 8.8]
print(min(floatValuesList))
print(max(floatValuesList))
print(sum(floatValuesList))

#Average 
print(f"The average is: {sum(floatValuesList)/len(floatValuesList)}")


cubelist = [(cube * cube * cube) for cube in range(1,9)]
print(cubesList)