import re

# Criteria:
# at least 8 characters
# Uppercase AND lowercase
# at least 1 digit

strong_pwd = re.compile(r'''(
(?=.*[A-Z])                     # Uppercase
(?=.*[a-z])                     # Lowercase
(?=.*[0-9])                     # at least 1 digit
.{8,}                           # at least 8 characters
)''', re.VERBOSE)

pwd = strong_pwd.search('Test4201')

if pwd == None:
    print ("Improve your password.")
else:
    print ("Your password is strong.")

# NOTE: Possible improvements include:
# Use input() to test different passwords from terminal
# Split the criteria and run separate checks to give better feedback to user
