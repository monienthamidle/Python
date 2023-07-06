bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)

# 0 1 2 3 4 5 6
colors = ['green','white','blue','red', 'yellow','purple','pink']
print(colors[0].title())
print(colors[1].title())
print(colors[2].title())
print(colors[3].title())
print(colors[4].title())
print(colors[5].lower())
print(colors[6].upper())
outputmessage = f'My favorite color is  {colors[-1].title()}'
print(outputmessage)
outputmessage = f'My favorite color is not {colors[0].title()}'
print(outputmessage)

colors[0] = 'orange'
colors[-2] = 'black'
print(colors)
colors.append('pink')
print(colors)
colors.append('purple')
print(colors)


colors = ['green','white','blue','red', 'yellow','purple','pink']
print(colors)
#note change
del colors[2]
print(colors)

poppedColor = colors.pop(-1)
print(poppedColor)
poppedColor = colors.pop(0)
print(poppedColor)


colors.remove('red')
print(colors)
