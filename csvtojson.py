import csv
import json

csvfile = open('./alexa/samples/top-1m.csv', 'r')
jsonfile = open('./alexa/samples/top-1m.json', 'w')

fieldnames_alienvault = ("ip", "risk", "reliability", "activity",
                         "country", "city", "geolocation", "No.")
fieldnames_alexa = ("alexa_score", "domain")

reader = csv.DictReader(csvfile, fieldnames_alexa, delimiter=',')
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
