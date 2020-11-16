import re
import sys
from os import path
import operator
import itertools

log_file_path = "server.log"
log_data = []

pattern = re.compile(r'\[(?P<time>.+)\](\s+\")(?P<requestType>\w+)(\s+)(?P<fileName>.*?)(\sHTTP)\/(?P<httpVersion>.*?)\"\s+(?P<httpResponse>\d+)\s(?P<bytes>\d+)')
fileDict = dict()

with open(log_file_path, "r") as file:
    for line in file:
        log_data.append(pattern.match(line).groupdict())

dedup_log_data = []
for i in log_data:
    if i not in dedup_log_data:
        dedup_log_data.append(i)

for item in dedup_log_data:
    key = item['fileName']
    value = int(item['bytes'])
    respCode = item['httpResponse']
    if (respCode == '200'):
        if key not in fileDict.keys():
            fileDict[key] = value
        else:
            oldValue = int(fileDict.get(key))
            value = oldValue+value
            fileDict[key] = value

sorted_fileDict = dict(sorted(fileDict.items(), key=operator.itemgetter(1)))
out_Dict = dict(itertools.islice(sorted_fileDict.items(), 10))
for k, v in out_Dict.items():
    print (str(k) +  " " + str(v))
