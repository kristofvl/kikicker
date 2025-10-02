# kikicker

Installing on a fresh Raspberry Pi 4B/5:
1. Run the [Raspberry Pi Imager](https://downloads.raspberrypi.com/imager/) and install `Other` -> `latest Raspberry Pi OS Lite (no desktop)` with ssh access as an extra setting
2. Once this is written to the sd card and running in the Raspberry Pi, connect to it via ssh
3. Update with: `sudo apt update && sudo apt upgrade -y`
4. Install LXQT and the sddm display manager: `sudo apt install -y lxqt sddm` (this might take a while)
5. Install xrdp: `sudo apt update && sudo apt install -y xrdp`
6. Install these Python packages: `sudo apt install python3-picamera2 python3-opencv `
7. Download our script: `wget https://raw.githubusercontent.com/kristofvl/kikicker/refs/heads/main/main.py`
