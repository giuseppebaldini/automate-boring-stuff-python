# Regex to match numbers with commas in groups of 3

import re

comma_regex = re.compile(r'''(
    (\d{1,3})                       # 1. One to three digits
    (,(\d){3})*                     # 2. Comma and 3 digits
    )''', re.VERBOSE)

num = comma_regex.search('42')
print (num.group(0))

# Regex to match full name of person whose surname is 'Nakamoto'

nakamoto_regex = re.compile(r'^[A-Z][a-z]+ Nakamoto')
