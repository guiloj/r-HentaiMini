import json
import os
import re
import time

try:
    import requests
except:
    permission: str = input(
        "The requests package is required for this program to work, install?(Y/N): "
    )
    if permission.lower() == "y":
        print("trying pip")
        os.system("pip install requests")
        print("trying pip3")
        os.system("pip3 install requests")
        try:
            import requests
        except:
            print("if nothing installed, please install it manually!")
            print("program quitting! please restart the program!")
            quit()
        print("done! program starting...")
    else:
        quit()

filesep: str = "\\" if os.name == "nt" else "/"

absFilePath: str = os.path.abspath(__file__)
os.chdir(os.path.dirname(absFilePath))

try:
    os.mkdir(os.path.join(os.path.dirname(absFilePath), "files"))
except OSError as error:
    print(error)
    path = os.path.join(os.path.dirname(absFilePath), "files")
    print(
        f'if the "{path}" directory already exists in this path please remove it or move the file'
    )
    quit()

URL1: str = "https://api.pushshift.io/reddit/search/submission/?subreddit=HentaiMini&sort=desc&sort_type=created_utc&after=1&before="
before: str = str(int(time.time()))
URL2: str = "&size=1000"

data: dict = json.loads(requests.get(f"{URL1}{before}{URL2}").text)
before: int = data["data"][-1]["created_utc"]
print("making requests...")
req: int = 1
while 1:
    req += 1
    subdata: dict = json.loads(requests.get(f"{URL1}{before}{URL2}").text)
    print(f"request num {req} done")
    if len(subdata["data"]) == 0:
        print("done")
        break
    data["data"] += subdata["data"]
    before: int = data["data"][-1]["created_utc"]

with open(f"files{filesep}fulldata.json", "wt", encoding="utf8") as f:
    f.write(json.dumps(data, indent=4))
print("json dumped")

links: list = []
imgurls: list = []

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

