# Import libraries
import os

# See if pip is already installed
os.system('cmd /c "python get-pip.py"') # Check for pip installed
os.system('cmd /c "pip install --upgrade pip"') # Upgrade or installed pip if not/it is installed

os.system('cmd /c "pip3 install pynput"') # Install pynput library

exec(open("info.py").read()) # Open second file for execution of script
