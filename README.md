# OSHE Growbot

The Growbot project was begun by Michigan Technological University's [Open Source Hardware Enterprise](http://openhardware.eit.mtu.edu/). You can find out more about this project on our [Appropedia page.](https://www.appropedia.org/OSHE_Growbot)

## Project Goal

The goal of this project is to manufacture a robot, about 1 cubic foot in size, that can automate the process of farming most garden crops. This would include tilling and planting the seeds, maintaining constant moisture and nutrient levels, and weeding around the plant. The robot will be made of 3D printed and easy to source components making it low-cost and available to be assembled by most home users. The growbot will be a time saver for users and make sure that plants get the correct amount of water and fertilizer at all times. The growbot will also be helpful for any homeowner that does small plot farming and has a busy lifestyle.

## Installation

### For Raspbery Pi OS, Ubuntu, or MacOS
```sh
# Make sure git is installed
sudo apt install -y git

# Clone and enter repository
git clone https://github.com/OSHE-Github/OSHE_Growbot growbot
cd growbot


# Run setup script
./first_time_setup.sh
```

### For Windows
```sh
# Clone and enter repository
git clone https://gitlab.com/mtu-most/most_openreactor
cd most_openreactor

# Update all submodules
git submodule update --init --recursive

# Create and configure python virtual enviroment
python3 -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

## Running
```sh
./start.sh
```

## Updating
```sh
git pull --all
git submodule foreach git pull
```

## Reseting python enviroment when done running
```sh
deactivate
```
