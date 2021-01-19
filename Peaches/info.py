# Import libraries
from pynput import mouse
import webbrowser
from time import sleep

# Define on_click to open tab with youtube video
def on_click (x, y, button, pressed):
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
listener1 = mouse.Listener(
    on_click = on_click)
listener1.start() # Start input listener
sleep(30)
listener1.stop() # Stop input listener