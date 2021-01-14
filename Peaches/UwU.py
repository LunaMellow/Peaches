import os

os.system('cmd /c "python get-pip.py"')
os.system('cmd /c "pip install --upgrade pip"')

os.system('cmd /c "pip3 install pynput"')
print("Successfully installed pynput")

exec(open("info.py").read())
