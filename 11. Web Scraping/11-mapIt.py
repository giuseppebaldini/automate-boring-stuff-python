#! python3
# mapIt.py: gets address from command line/clipboard and opens it in Google Maps
# Using webbrowser, a built-in module able to open a browser

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
