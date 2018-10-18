colors = []

while True:
    color = input('Enter the name of the colors you know, starting from number'
          + str(len(colors) + 1) + ' or type nothing to stop: ')
    if color == '':
        break
    colors = colors + [color]

print('The colors are: ')
for color in colors:
    print(color)
