#!/bin/bash

# Update all submodules
#git submodule update --init --recursive

# Install needed dependancies
sudo apt update; sudo apt upgrade -y
sudo apt install -y python3-venv sqlite3 npm

# Create and configure python virtual enviroment
python3 -m venv .venv
source .venv/bin/activate
pip install wheel
pip install -r requirements.txt

# Install NPM packages
#npm i ./static
