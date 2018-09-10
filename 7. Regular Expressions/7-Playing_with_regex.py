import re

# Creating a Regex object for phone numbers

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.search('My number is 415-555-4242.')
'Phone number found: ' + mo.group()

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 415-555-4242.')

mo.group(1)
mo.group(2)
mo.group(0)
mo.groups()

# Assign different groups to different variables

area_code, main_num = mo.groups()

# Match parentheses

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)

# Using the pipe to maatch one OR the other

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()

# Using the pipe | for common instances (e.g. prefixes)

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()

# ? = Optional mathching (0 or 1)

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
'Batwoman'

# * = Optional matching (0 to many)

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

# + = One or more

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()

# {} = Repetitions mathching {n} = only n repetitions
# {n,m} = from n to m repetitions (e.g. {1.6})

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()

# NOTE: Py regex are greedy by default - match longest string

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()

# Use findall() to return all the matches

# No groups = List of strings
# Groups = List of tuples

# NOTE: You can make your own character classes

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Robocop eats baby food. BABY FOOD.')

>>> ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

# Using ^ will create a negative class
