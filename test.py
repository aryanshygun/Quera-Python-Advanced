import requests


def process(url):
    data = requests.get(url)
    if data.status_code != 200:
        return 'Bad Query'
    xdict = {}
    for i in data.json():
        xdict[i["category"]] = xdict.get(i["category"], 0) + 1
    
    if len(xdict.keys()) == 1:
        return license(xdict.keys())[0]
    return "I can't recognize it"
    

xlist = [
    {"name": "The Road to Reality", "category": "physic"},
    {"name": "Something Deeply Hidden", "category": "physic"}
]

xdict = {}

for i in xlist:
    xdict[i["category"]] = xdict.get(i["category"], 0) + 1

print(xdict)

if len(xdict.keys()) == 1:
    print(xdict.keys())