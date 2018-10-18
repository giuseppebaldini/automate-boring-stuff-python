# Finding your number

print ('Hello there! I need your help again.')
print ('Please let me calculate your number')

age = int(input('How old are you? '))

if age < 18:
    print ("Sorry, you are too young to have a number.")
else:
    height = int(input('How tall are you in cm? '))

magic_num = round((age + height)/42)

print ("Great! Your number is ") magic_num
