import time
import pyautogui
import tkinter as tk

def screenshot():

    name = int(time.time())
    name = str(name)
    time.sleep(2)
    img = pyautogui.screenshot(name+"test.png")
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take Screenshot",
    command = screenshot

)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text = "Quit",
    command = quit
)
close.pack(side=tk.LEFT)
root.mainloop()
