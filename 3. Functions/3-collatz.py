def collatz(number):
    
    if number % 2 == 0:
        print (number // 2)
        return number // 2
    else:
        odd = 3 * number + 1
        print (odd)
        return odd

try:
    n = input('Enter number: ')
    while n != 1:
        n = collatz(int(n))
        
except ValueError:
    print('Error: please enter an integer.')
