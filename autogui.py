import pyautogui as pg
import time
import os

from pc_check import get_ip_addr
import settings

def run_app():
    os.startfile(r"C:\Users\Sirius\Desktop\tnav\tNavigator222.exe")

def open_model():
    # set active window
    time.sleep(3)
    pg.click(903,15)
    time.sleep(1)

    # open model file
    pg.hotkey("ctrlleft", "o")
    time.sleep(1)
    
    # change path to data
    # top
    pg.click(613,89)
    pg.hotkey("ctrlleft", "a")
    pg.hotkey("backspace")
    pg.typewrite(r"C:\Users\Sirius\Desktop\project\data")
    pg.hotkey('enter')
    time.sleep(1)

    # down
    pg.click(368, 552)
    pg.typewrite("BRUGGE.DATA")
    pg.hotkey('enter')

def run_simulation():
    time.sleep(8)
    pg.click(338, 77)

def wait_simulation():
    time.sleep(85)

def save_res():
    # open editor
    pg.click(1899, 192)
    time.sleep(1)

    # change filename
    pg.click(848, 296)
    pg.hotkey("ctrlleft", "a")
    pg.hotkey("backspace")

    pg.typewrite(rf"C:\Users\Sirius\Desktop\project\results\sim_pc{(settings.hosts + settings.workers).index(get_ip_addr())}.txt")


    # click load selection
    pg.click(352, 758)
    time.sleep(1)

    # top
    pg.click(896, 338)
    pg.hotkey("ctrlleft", "a")
    pg.hotkey("backspace")
    pg.typewrite(r"C:\Users\Sirius\Desktop\project")
    pg.hotkey('enter')
    time.sleep(1.5)

    # down
    pg.click(645, 803)
    pg.typewrite("filter.txt")
    pg.hotkey('enter')

    pg.click(1486, 768)
