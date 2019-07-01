import os
import json

path = 'out\\'

dictFile = {}

# read the file image in out directory
for r, d, f in os.walk(path):
    for file in f:
        # add new instance in dictionary
        dictFile[file] = file.split('_')[0]

# print(dictFile)

# dump Dictionary in to Json Object File with UTF8 format and turn off ascii option
with open('result.json', 'w', encoding='utf8') as fp:
    json.dump(dictFile, fp, ensure_ascii=False)
