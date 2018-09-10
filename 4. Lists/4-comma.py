spam = ['apples', 'bananas', 'pear', 'peach', 'cats']

def comma(x):
    for i in range(0, len(x)-1):
        i = str(x[i]) + ', '
        print(i, end=""),
    print ('and ' + x[-1])

comma(spam)
