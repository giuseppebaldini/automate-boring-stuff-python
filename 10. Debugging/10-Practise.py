# Chapter 10 - Debugging
# NOTE: Use try and except to handle errors

# If traceback info is needed but we want to handle the exception
# it is possible to use traceback.format_exc() from the traceback module

# Example
import traceback
try:
    raise Exception('This is the error message')
except:
    errorFile = open(error_log.txt, 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to error_log.txt')

# Assertions
# Example

podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

# Basically, an assert statement says: “I assert that this condition holds true,
# and if not, there is a bug somewhere in the program.”
# If assert statement fails, program SHOULD CRASH.
