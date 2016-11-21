# Iris_recog
Iris detection project for AE663

This is an Iris Detection project for the subject AE663 in our college. The project code is implemented in Python scripts. The code is meant to be run in Python 3.5; NO SUPPORT FOR PYTHON-2 COMPATIBILITY IS ADDED.

### Pre-requisites for this toolbox:

1. Python 3.5 or compatible.
2. Scikit-Image, available with the following shell command:
    - Linux and MacOS users: pip install -U scikit-image
    - Windows: instructions are available at [Scikit-Image installation help]
3. OpenCV, of which a specific version has been used.(this will be changed in future upgrades)
    - Ubuntu users can run the Makefile and obtain the relevant software. The download will take several hours and a lot of disk space.
    - Other OS implementations have not been done yet, but we are planning to scrap the use of PIL and OpenCV, and replace both by Scikit-Image only. (this may need some time and work).
4. Tkinter for Python 3.5, available with the following shell command:
    - Ubuntu/Debian users may use the command: **sudo apt-get install python python-tk idle python-pmw python-imaging**
    - Fedora users may use **yum install tkinter**.
    - Further details are available at the url [Tkinter installation for Python 3].

### Files in this project:

1. The project is in Python, and all Python scripts are included in the **codes** folder.
    - The files **main.py**, **gui.py** and **iris_pos.py** are end testing files. See the **Automation and database experiment** section of this README.
2. The project can be tested using Unit-Test code in the file **test_checker.py**.
3. The documentation of all the files have been generated using **Sphinx** and are in the **documentation** folder, in HTML format.

### Automation and database experiment:

- A simple database program has been inserted here for the benefit of the user. It is implemented via the text-based script **main.py** and the GUI-based script **gui.py**. Both allow the user to insert new images of human eyes in the human eye image database included here, and also to check new images against existing images in the database.
- The purpose of both is to test the efficiency of this toolset against a variety of eye images. Please feel free to use it on as many eye images as possible. If an error is found in the recognition of iris, reporting the same on our GitHub page will be highly appreciated.
- The user is adviced to run **make clean** after running these files, to remove unneccessary .pyc files and pycache, unless it is desired to keep them for the purpose of speeding up future runs of the scripts.

### Contact us:

1. Our email addresses are as follows:
    - Soumallya Chatterjee [sbchat13@gmail.com]
    - Rajarshi Bandopadhyay [theocrat93@gmail.com]
    
    [Scikit-Image installation help]: <http://www.lfd.uci.edu/~gohlke/pythonlibs/#scikit-image>
    [Tkinter installation for Python 3]: <http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter>
    [sbchat13@gmail.com]: <sbchat13@gmail.com>
    [theocrat93@gmail.com]: <theocrat93@gmail.com>
