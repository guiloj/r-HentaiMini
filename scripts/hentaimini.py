import json
import requests
import os
import re
import time

filesep = "\\" if os.name == "nt" else "/"

os.chdir(os.path.dirname(__file__))
try:
    os.mkdir(os.path.join(os.path.dirname(__file__), "files"))
except OSError as error:
    print(error)
    path = os.path.join(os.path.dirname(__file__), "files")
    print(
        f'if the "{path}" directory already exists in this path please remove it or move the file'
    )
    quit()

url1 = "https://api.pushshift.io/reddit/search/submission/?subreddit=HentaiMini&sort=desc&sort_type=created_utc&after=1&before="
before = str(int(time.time()))
url2 = "&size=1000"

data = json.loads(requests.get(f"{url1}{before}{url2}").text)
before = data["data"][-1]["created_utc"]
print("making requests...")
req = 1
while 1:
    req += 1
    subdata = json.loads(requests.get(f"{url1}{before}{url2}").text)
    print(f"request num {req} done")
    if len(subdata["data"]) == 0:
        print("done")
        break
    data["data"] += subdata["data"]
    before = data["data"][-1]["created_utc"]

with open(f"files{filesep}fulldata.json", "wt", encoding="utf8") as f:
    f.write(json.dumps(data, indent=4))
print("json dumped")
links = []
imgurls = []

for x in data["data"]:
    try:
        links.append(x["full_link"] + "\n")
    except KeyError:
        links.append("0\n")
    try:
        for i in (".jpg", ".png", ".gif", ".jpeg"):
            if "external-preview.redd.it" in x["url"]:
                raise KeyError
            if x["url"].endswith(i):
                break
            if re.search(r"(.(?:jpeg|png|jpg|gif)\?(?:[0-9]+))", x["url"]):
                break
        else:
            raise KeyError
        imgurls.append(x["url"] + "\n")
    except KeyError:
        imgurls.append("0\n")

print("links/imgs filtered")

with open(f"files{filesep}links.txt", "wt", encoding="utf8") as f:
    f.writelines(links)

with open(f"files{filesep}imgs.txt", "wt", encoding="utf8") as f:
    f.writelines(imgurls)

print("links/imgs dumped")
print("program done")
