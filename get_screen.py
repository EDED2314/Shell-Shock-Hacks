import win32gui
import time
from PIL import ImageGrab
import numpy as np
import cv2


def enum_cb(hwnd, results):
    results.append((hwnd, win32gui.GetWindowText(hwnd)))
    
def get_screens(screen_name):
    winlist = []
    win32gui.EnumWindows(enum_cb, winlist)
    screens = [(hwnd, title) for hwnd, title in winlist if screen_name in title.lower()]
    return screens

def get_screen_data(window_name: str):
    screens = get_screens(window_name)
    
    window = screens[0][0]

    screen_image = np.array(ImageGrab.grab(bbox=win32gui.GetWindowRect(window)))
    return screen_image
