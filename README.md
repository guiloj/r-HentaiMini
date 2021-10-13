# [r-HentaiMini](https://github.com/guiloj/r-HentaiMini/)

## requirements
- [python3](https://www.python.org/downloads/)
- [requests](https://pypi.org/project/requests/) _(can be automatically installed)_

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
#### ([better automatic C# version](https://github.com/AnimeTheNeko/FileDownloader) by @AnimeTheNeko)
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
* if you do not have [curl](https://curl.se/windows/) on your windows computer you can [download it here](https://curl.se/windows/) and add it to your computer's path, but [curl](https://curl.se/windows/) should be on windows by default
