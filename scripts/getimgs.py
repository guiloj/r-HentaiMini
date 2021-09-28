import os

absFilePath = os.path.abspath(__file__)
os.chdir( os.path.dirname(absFilePath) )
filesep = "\\" if os.name == "nt" else "/"
if not os.path.isdir("files") or not os.path.isfile(f"files{filesep}imgs.txt"):
    print(
        'the "files" directory was not found or is incomplete, please move this file to the correct directory or run "hentaimini.py" again'
    )
    quit()
try:
    os.mkdir(os.path.join(os.path.dirname(absFilePath), "imgs"))
except OSError as error:
    print(error)
    path = os.path.join(os.path.dirname(absFilePath), "imgs")
    print(
        f'if the "{path}" directory already exists in this path please remove it or move the file'
    )
    quit()
with open(f"files{filesep}imgs.txt", "rt", encoding="utf-8") as f:
    content = f.readlines()
os.chdir(os.path.dirname(absFilePath) + filesep + "imgs")

for x, y in zip(content, range(len(content))):
    if "0" in str(x):
        continue
    for typ in (".jpg", ".png", ".gif", ".jpeg"):
        if typ in x:
            mtype = typ
            break
    else:
        mtype = '.jpg'
    if os.name != 'nt':
        os.system(f"wget -O img{y}{mtype} {x}")
    else:
        os.system(f"curl -o img{y}{mtype} {x}")
