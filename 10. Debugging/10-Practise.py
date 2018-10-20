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
# and if not, there is a bug somewhere in the program.
# If assert statement fails, program SHOULD CRASH.

# Example: traffic light simulation

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

# We can use an assertion to make sure that one of the lights is always red
assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

# NOTE: You can add an -o option when running Python to disable assertions

# Using the logging module to understand code outputs and in which order
# NOTE: Put this under the #! Python shebang line

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -
%(message)s')

# NOTE: 5 levels of logging levels

1. DEBUG
2. INFO
3. WARNING
4. ERROR
5. CRITICAL

# Disable them with:
logging.disable(logging.CRITICAL)

# Disable from a level and below:
logging.disable(logging.LEVEL)

# Optionally, it is possible to log in a file
logging.basicConfig(filename = 'program_logFile.txt', level=logging.DEBUG,
format=' %(asctime)s - %(levelname)s - %(message)s')
