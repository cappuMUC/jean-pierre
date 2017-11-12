# Setup
**More details to come on the soon-to-come Jean-Pierre's doc !!**
* Clone this repository : `git clone https://github.com/matteocargnelutti/jean-pierre.git`
* Please run *install.sh* : `cd jean-pierre`, then `chmod a+x install.sh` and `./install.sh`
* During setup, a configuration assistant will prompt, asking for basic configuration information. You can choose if you want to use a **buzzer** or not : if you do, you will have to specify on which **GPIO Pin** it is connected.
* At the end of the setup script, Jean-Pierre's scanner and web server will be running : please note that, from startup, **Jean-Pierre could take up to 2 minutes to boot on a 2017 Pi Zero W**.

# Manual install / uninstall guide
- To do

# Processes
**Jean-Pierre is made of three separate processes that are meant to run in parallel.**
* **config** : the configuration assistant.
* **scanner** : Process that scans the products with the camera.
* **web** : Flask app that handles the web application, launched through *gunicorn*.

## Manually launch processes
**Processes are automaticaly handled by both supervisor and the install script. But in case you want to launch it separately :**
* `python jeanpierre.py --do config` : launches the configuration assistant.
* `python jeanpierre.py --do scanner` : launches the scanner. *Shortcut :* `./scanner.sh`
* `python jeanpierre.py --do webdebug` : launches the web app process in DEBUG mode.
* `gunicorn --bind 0.0.0.0 jeanpierre:webapp` : launches the web app process in production mode. *Shortcut :* `./web.sh`

# Database structure
* **Jean-Pierre** uses a SQLite3 database, stored as **database.db** at the project's root.

Table | Use
------| ---
`Params` | Contains config parameters
`Products` | Local products database, contains items scanned and found on OpenFoodFacts, as well as user-created items
`Groceries` | Grocery list, based on the products table


# Shared parameters
Key | Value
----| -----
`buzzer_on` | Should Jean-Pierre try to use a buzzer ?
`buzzer_port` | On which GPIO port the buzzer is ? 
`camera_res_x` | Camera's resolution : width
`camera_res_y` | Camera's resolution : height
`user_password` | Password for the web interface (cyphered)

* Theses parameters are defined using the config assistant, run : `python jeanpierre.py --do config`.
* They are stored into the **Params** database table.

# Products data source :
* All products data, including pictures, come from the *OpenFoodFacts API* : https://world.openfoodfacts.org/data

# Dev : PC Mode
* Define an environnement variable `PC_MODE` if you wish to work on this project's code on your PC : it deactivates the import of RPi.GPIO and PiCamera

# Hardware
**Hardware used :**
* Raspberry Pi Zero W
* Raspberry Pi Camera Module V2
* A random *buzzer* module

You can specify during setup if you want to use a buzzer or not : if you do, you will have to specify on which **GPIO Pin** it is connected.

This project should run on any Raspberry Pi model that can handle the PiCamera module.

# Software dependencies
## OS
* Raspbian (lite)

## sudo apt-get install ...
* python3-dev
* python3-pip
* python3-picamera
* git
* virtualenv
* libzbar0
* supervisor
* libjpeg8-dev

## pip dependencies (see requirements.txt)
* picamera
* pyzbar
* pyzbar[scripts]
* pytest
* requests
* RPi.GPIO
* flask
* gunicorn

# Notes to write
* A note about camera focus adjustement (and how it could break the camera)
* A note about the web server security and how it shouldn't be used in production (no https !)