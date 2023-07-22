import urllib.request as task
import json
import csv

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with task.urlopen(src)as response:
    data=json.load(response)

finaldata=data["result"]["results"]

with open("attraction.csv", mode="w", newline="", encoding="utf-8")as file:
    attraction=csv.writer(file)

    for final in finaldata:

        address=final["address"][5:8]

        pic=final["file"].split("https://")[1]
        newpic="https://"+pic

        attraction.writerow([
            final["stitle"],
            address,
            final["longitude"],
            final["latitude"],
            newpic,
        ])

newdic={}
for dic in finaldata:
    mrt=dic["MRT"]
    title=dic["stitle"]
    if mrt in newdic:
        newdic[mrt].append(title)
    else:
        newdic[mrt]=[title]

with open("mrt.csv", mode="w", newline="", encoding="utf-8")as file1:
    mrt=csv.writer(file1)

    for MRT, STATION in newdic.items():
        mrt.writerow([MRT]+STATION)

