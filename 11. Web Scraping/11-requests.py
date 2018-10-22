# requests.get() takes a string of a URL to download

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code == requests.codes.ok
# Status code 200 = OK | Status code 404 = Not Found
print(res.text[:250])

# To raise an exception in case of URL not found
res.raise_for_status()

# In case the failed download should NOT stop the program, we can use
try:
    res.raise_for_status()
except Exception as exc:
    print('There was an error: %s' % (exc))

# To write a webpage in a file, we will need to use the 'wb' write binary mode
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('Romeo_and_Juliet.txt, 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
