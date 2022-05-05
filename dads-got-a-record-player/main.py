import myers
import requests
from bs4 import BeautifulSoup
import json
import csv
import time

print("Hey dad! Let's get some records")
print("Fetching Page")

url = 'https://millpondrb.ca/records_list.html'
page = requests.get(url)

print("Page Recieved! Parsing")

soup = BeautifulSoup(page.content, 'html.parser')

listElements = soup.findAll('tr')
listHeaders = soup.findAll('th')

data = []
headers = [
    'ID',
    'Attribute',
    'Artist',
    'Album Name',
    'Price',
    'Spec',
    'Goodness',
    'Condition',
    'Category',
    'Year'
]

# adding the list headers
# for header in listHeaders:
#   headers.append(header.text)

data.append(headers)
for row in listElements:

    # if its a vinyl
    if row.select_one(':nth-child(2)').text == 'Vinyl':

        data.append([])
        # add to the json
        for dataPoint in row:
            if dataPoint.text.strip():
                data[-1].append(dataPoint.text)

with open('json.json', 'r') as f:
    oldData = json.load(f)

with open('old.json', 'w') as outfile:
    json.dump(oldData, outfile)

with open('json.json', 'w') as outfile:
    json.dump(data, outfile)

diff = myers.diff(oldData, data, context=None, format=None)

removed = []
added = []

for i in diff:
    if i[0] == 'i':
        added.append(i[1])
    if i[0] == 'r':
        removed.append(i[1])

with open('diff.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(headers)

    if (added):
        write.writerow(["ADDED"])
        write.writerows(added)
    if (removed):
        write.writerow(["REMOVED"])
        write.writerows(removed)

    if ((not added) and (not removed)):
        write.writerow(["Hi Dad. There are no changes."])

print("Completed... Results in './diff.csv'")
print("Program Terminating")
time.sleep(2)