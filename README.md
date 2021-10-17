# [r-HentaiMini](https://github.com/guiloj/r-HentaiMini/)

---

# [ImgDownloader](https://github.com/guiloj/r-HentaiMini/blob/main/ImgDownloader)

##### ([better (windows) automatic C# version](https://github.com/AnimeTheNeko/FileDownloader) by @AnimeTheNeko)

## [Windows](https://github.com/guiloj/r-HentaiMini/blob/main/ImgDownloader/Windows)

### .exe

To use the Windows version of the program you need to follow the following instructions:

-   Download the [windows.exe.zip](https://github.com/guiloj/r-HentaiMini/releases/latest/) zip file
-   Place the zip file in your chosen directory and extract it
-   Execute the `ImgDownloaderCS.exe` file
-   On this screen:

    ![test](https://manula.r.sizr.io/large/user/1894/img/tnt.png)

    -   Press `More info` and `Run anyway` (windows thinks this is a virus because it is not on their whitelist)

        ![test](https://www.redcort.com/assets/imgs/pages/blog/2018/windows-defender.png)

-   You can now read what is in the screen and press <kbd>Enter</kbd>
-   Wait for the program to finish and press <kbd>Enter</kbd> again to exit the program
-   Have fun!

#### Warnings:

-   The program will create a directory called `imgs` where it was placed, so plan where to put the executable
-   The program needs about 2gigs of space to complete the download process.
-   All the `.dll` and `.json` files are crucial for the program, do not delete them

### .cs

To compile and use the `Program.cs` you will need to follow the following instructions:

-   Install [Visual Studio 2019 Community Edition](https://visualstudio.microsoft.com/downloads/)
-   Select the `.NET desktop development` workload and let it install
-   Create a new project and choose `Console app (.NET core)` for C#
-   Name your project
-   Choose `.NET 5.0` (or 3.1 and use the Unix `Program.cs`) and proceeed
-   Now you can download the [windows.cs.zip](https://github.com/guiloj/r-HentaiMini/releases/latest/) zip file and extract it into your preferred directory
-   You can now copy the contents of the `Program.cs` file to the file in Visual Studio or move it instead
-   Inside Visual Studio on the top left change the mode from `Debug` to `Release`
-   Now press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd> to build the program
-   Go to the path specified in the build console and find the bin, there you can find the compiled `[ProjectName].exe`

## [Unix](https://github.com/guiloj/r-HentaiMini/blob/main/ImgDownloader/Unix)

### .exe (yeah lol)

To use the already compiled program you need to follow the following instructions:

-   Download the [unix.exe.zip](https://github.com/guiloj/r-HentaiMini/releases/latest/) zip file and extract it into your preferred directory
-   You can now run the program using one of the following commands:
    -   using mono
        ```sh
        mono ImgDownloader.exe
        ```
    -   using wine
        ```sh
        wine ImgDownloader.exe
        ```

### .cs

To compile and use the `Program.cs` you will need to follow the following instructions:

-   Download the [unix.cs.zip](https://github.com/guiloj/r-HentaiMini/releases/latest/) zip file and extract it into your preferred directory
-   Now you can run the `install.sh` file if you run a Debian based system e.g: Ubuntu
-   Otherwise you will need to install the `mono-complete` package using the package manager of your distro / MacOs
-   Now execute the following commands:

    ```sh
    mcs -out:ImgDownloaderCS.exe Program.cs
    ```

    ***

    ```sh
    mono ImgDownloaderCS.exe
    ```

    or

    ```sh
    wine ImgDownloaderCS.exe
    ```

---

# [Python Scripts](https://github.com/guiloj/r-HentaiMini/blob/main/scripts)

## requirements

-   [python3](https://www.python.org/downloads/)
-   [requests](https://pypi.org/project/requests/) _(can be automatically installed)_

## usage

### hentaimini.py

-   place the [`hentaimini.py`](https://github.com/guiloj/r-HentaiMini/blob/main/scripts/hentaimini.py) script in your desired directory
-   make sure there is no `files` directory inside the cwd, if there is, delete it or move the file
-   open a terminal window in the current directory and execute:
    ```sh
    python3 hentaimini.py
    ```
-   wait for the program to execute
-   done!

### getimgs.py

#### ([better automatic C# version](https://github.com/AnimeTheNeko/FileDownloader) by @AnimeTheNeko)

-   Place the [`getimgs.py`](https://github.com/guiloj/r-HentaiMini/blob/main/scripts/getimgs.py) script in the same directory that [`hentaimini.py`](https://github.com/guiloj/r-HentaiMini/blob/main/scripts/hentaimini.py) was executed
-   Make sure there is no `imgs` directory inside the cwd, if there is, delete it or move both the file and the `files` directory
-   Open a terminal window in the current directory and execute:
    ```sh
    python3 getimgs.py
    ```
-   Wait for the program to execute
-   Done!

## warnings

-   I run Ubuntu on my computer so these scripts may not work properly on Windows (they should work tho)
-   The [`getimgs.py`](https://github.com/guiloj/r-HentaiMini/blob/main/scripts/getimgs.py) script will create a very big directory, only 660 images were about 550mb of space
-   If you do not have [curl](https://curl.se/windows/) on your windows computer you can [download it here](https://curl.se/windows/) and add it to your computer's path, but [curl](https://curl.se/windows/) should be on windows by default
