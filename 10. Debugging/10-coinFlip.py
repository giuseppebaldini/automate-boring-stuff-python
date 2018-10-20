import random
   heads = 0
   for i in range(1, 1001):
     if random.randint(0, 1) == 1:
           heads = heads + 1
       if i == 500:
           print('Halfway done!')
   print('Heads came up ' + str(heads) + ' times.')

# In this case, it would be more useful to add a Breakpoint within the loop
# to avoid checking every single iteraction
