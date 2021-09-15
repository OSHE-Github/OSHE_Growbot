#!/bin/bash

# Update all submodules
#git submodule update --init --recursive

# Install needed dependancies
sudo pacman -Syyu
sudo pacman -S sqlite3 npm

# Create and configure python virtual enviroment
cd static
python3 -m venv venv
source venv/bin/activate
pip install wheel
pip install -r requirements.txt

# Install NPM packages
npm i
