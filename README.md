# [r-HentaiMini](https://github.com/guiloj/r-HentaiMini/)

## requirements
- [python3](https://www.python.org/downloads/)

## usage

### hentaimini.py
* place the [`hentaimini.py`](https://github.com/guiloj/r-HentaiMini/blob/main/scripts/hentaimini.py) script in your desired directory
* make sure there is no `files` directory inside the cwd, if there is, delete it or move the file
* open a terminal window in the current directory and execute:
  ```
  python3 hentaimini.py
  ```
* wait for the program to execute
* done!
### getimgs.py
* place the [`getimgs.py`](https://github.com/guiloj/r-HentaiMini/blob/main/scripts/getimgs.py) script in the same directory that [`hentaimini.py`](https://github.com/guiloj/r-HentaiMini/blob/main/scripts/hentaimini.py) was executed
* make sure there is no `imgs` directory inside the cwd, if there is, delete it or move both the file and the `files` directory
* open a terminal window in the current directory and execute:
  ```
  python3 getimgs.py
  ```
* wait for the program to execute
* done!

## warnings

* I run Ubuntu on my computer so these scripts may not work properly on Windows (they should work tho)
* the [`getimgs.py`](https://github.com/guiloj/r-HentaiMini/blob/main/scripts/getimgs.py) script will create a very big directory, only 660 images were about 550mb of space
* if you have [wget](http://gnuwin32.sourceforge.net/packages/wget.htm) on your windows computer you can modify the [`getimgs.py`](https://github.com/guiloj/r-HentaiMini/blob/main/scripts/getimgs.py) script to look like this:
#### modified:
```python3
for x in content:
    if str(x) == "0":
        continue
    os.system(f"wget {x}")
```
#### original:
```python3
indx = 0
for x in content:
    if str(x) == "0":
        continue
    if os.name != "nt":
        os.system(f"wget {x}")
    else:
        with open(f"pic{indx}.jpg", "wb") as handle:
            response = requests.get(x, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
        indx += 1
```
