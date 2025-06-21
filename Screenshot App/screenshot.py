import time
import pyautogui
import tkinter as tk

# defining the Screenshot function which will take screenshot at specified folder
def screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/Swapnil/Downloads/python_project/screenshot_app/screenshot_data/{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()

# Creating GUI for Screenshot action

# creating frame for GUI
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

#adding take screenshot button inside the frame
button = tk.Button(
    frame,
    text = 'Take Screenshot',
    command = screenshot 
)

#adding Quit button to close the GUI
button.pack(side = tk.LEFT)
close = tk.Button(
    frame,
    text = 'QUIT',
    command = quit 
)
close.pack(side = tk.LEFT)

root.mainloop()