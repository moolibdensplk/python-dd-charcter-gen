# D&D Character Sheet Generator
Python + PYQT5 Basic tool to generate a simple character sheet for Dungeons and Dragons.<br>
The character sheet will include:
- character attributes (STR, DEX etc...)
- attribute modifiers
- saving throw modifiers
- character's name
- character's class (Wizard, Rogue etc)
- character's race (Human, Dwarf etc)
- character's hit points

Attributes and hit points can be re-rolled (there is a button to do that).

Once happy with it - hit the "Generate Character Sheet" button, and it will create a PDF file containing your character's details plus a few other fields you can then fill up later with a pen !

The output PDF file will be located in:<br>
`./character_sheets/<character_name>.pdf` file
If you do not choose a name, the file will be named: UNNAMED_CHARACTER.pdf :)

## Requirements
This tool has been written using:

* Python 3.11.4
* PyQT5 (5.15.9)
* pyqt5-tools (5.15.9.3.3)
* * PyQT5 Designer (provided by pip package: pyqt5-tools)

## How To Install
### Linux / MacOS
These steps assume that you have the `penv` tool installed and configured on your machine. 

* Install Python 3.11.4 first, I used `pyenv` (on MacOS X)
```
pyenv install 3.11.4
```

* Create a virtual env using pyenv
```
pyenv virtualenv 3.11.4 dd_charcter_gen_app
```

* Activate the env
```
pyenv activate 3.11.4/envs/dd_charcter_gen_app
```

* Install all dependencies
```
pip install --upgrade pip
pip install pyqt5
pip install pyqt5-tools
```

* checkout the code from the repo
```
git clone git@github.com:moolibdensplk/python-dd-charcter-gen.git 
```

or download it as ZIP and uncompress...

```
cd <folder with the code>
```

* Run the code:
```
python main.py
```

### WINDOWS steps (tested on Windows 10 64bit Home edition)

* Download Python 3.11.4 (that's the version I used to write it. It should work with other newer 3.x versions. It WILL NOT work with python 2.7 / 2.x !!)

Windows 64 bit
https://python.org/downloads/release/python-3114/python-3.11.4-amd64.exe

Windows 32 bit:
https://python.org/downloads/release/python-3114/python-3.11.4.exe

* Install python using the installer downloaded from one of the links above
  Make sure you TICK the checkbox on the first screen to add python.exe to your PATH:

* before installing all the required python dependencies, you will need to also install the following tool, that is REQUIRED by this code:
  **wkhtmltopdf** , you can find it here: <br>
https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.msvc2015-win64.exe


* Now update pip tool using:
  (you will use it to install python modules needed for this app to run

```
pip install --upgrade pip
```

#### Download and Unzip the app codebase from github:

* Go to:  https://github.com/moolibdensplk/python-dd-charcter-gen

  Click CODE => Download Zip
  Open the command windows CMD shell:

  START => type `cmd` in the search textbox next to start / windows flag button

  in the CMD type :

  ```
  c:\
  cd \Users\<yourWindowsUsername>
  mkdir PythonProjects
  cd PythonProjects
  ```

* Now unzip the downlaoded APP zip file, and drag the resulting folder to c:\Users\<yourWindowsUsername>PythonProjects\

* in CMD window, enter the unzipped code directory by typing:

  ```
  cd python-dd-charcter-gen-main
  ```
  You should now be inside the following path (`c:\Users\<yourWindowsUsername>\PythonProjects\python-dd-charcter-gen-main\`)

#### Install and configure a Python Virtual Environment
(to keep your python installation nice and tidy)

* Now install virtualenv module
  ```
  pip install virtualenv
  ```

* Create a virtual environment:
  ```
  virtualenv dd_charcter_gen_app
  ```
  *IMPORTANT:* The above command will create a folder named after the virtual envirobnemnet name you have specified above (in this case: `list-builder-venv`) exactly INSIDE the current folder you are in.
  If you followed the steps correctly, you should see:
  `c:\Users\<yourWindowsUsername>\PythonProjects\python-dd-charcter-gen-main\dd_charcter_gen_app`

* Activate the virtual env you created

  ```
  .\dd_charcter_gen_app\Scripts\activate.bat
  ```

  *IMPORTANT:* after you run that command, you should see: `(dd_charcter_gen_app)` added in front of your command line prompt, like this:
  ```
  (dd_charcter_gen_app) C:\Users\<yourUserName>\PythonProjects\python-dd-charcter-gen-main>
  ```
* Install PYTHON modules needed by the code:
  ```
  (dd_charcter_gen_app) C:\Users\<yourUserName>\PythonProjects\python-dd-charcter-gen-main> pip install -r requirements.txt
  ```

* Run the python.exe to launch the app:

  ```
  python.exe main.py
  ```
  Once you run this, you should see a main app window...

* Once finished using the app, DEACTIVATE the virtual environment:
  ```
   deactivate
  ```
  *IMPORTANT:* your prompt will fo back to normal the `(dd_charcter_gen_app)` part will disapear.
  If you want to activate it again, make sure you are in the right path and run activate again:
  ```
  cd C:\Users\<yourUserName>\PythonProjects\python-dd-charcter-gen-main>
  .\dd_charcter_gen_app\Scripts\activate.bat
  ```
  

## DISCLAIMER :
This app is not even an ALPHA version !
Purely EXPERIMENTAL code.
I take NO RESPONSIBILITY for any issues - use it on your own.
If you don't like something - feel free to fork the repo and write a better version :)
