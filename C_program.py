from tkinter import *
from threading import Thread
import subprocess
import pyautogui
import os
import time
from datetime import datetime, timedelta

from Keylogger import Keylogger, write_to_file
from pass_work import get_pass_work
from Time import check_time_use
from Time import time_can_use
from Time import time_delta_can_use
from Time import time_now
from Time import get_list_time
from Time import to_day

flag = False
num_enter_pass_work = 0
p_pass_work, c_pass_work = get_pass_work("passwork.txt")
list_time = get_list_time("time.txt")


def shut_down(seconds):
    time.sleep(seconds)
    global flag
    # print(flag)
    if flag:
        subprocess.Popen("shut_dow.bat")

def destroy_app(scr, seconds):
    time.sleep(5)
    scr.destroy()

def screen_shot(seconds):
    while True:
        str_time = datetime.now()
        end_time = datetime.now() + timedelta(seconds=seconds)
        while True:
            if end_time <= datetime.now():
                screenshot = pyautogui.screenshot()
                path = to_day() + "/screen_shot"

                if not os.path.exists(path):
                    os.makedirs(path)
                path += "/" + time_now() + ".png"
                screenshot.save(path)
                break
    
def check_file_time(seconds):
    while True:
        time.sleep(seconds)
        global list_time
        now_list_time = get_list_time("time.txt")
        if now_list_time != list_time:
            list_time = now_list_time
            change_file_time = Tk()
            change_file_time.attributes('-fullscreen', True)
            change_file_time.columnconfigure(0, weight=1, minsize=76)
            change_file_time.rowconfigure(0, weight=1, minsize=50)
            label_change = Label(change_file_time, text="change\n" + time_can_use('time.txt'))
            label_change.grid(row=0, column=0)
            Thread(target=destroy_app, args=(change_file_time, 10))
            change_file_time.mainloop()


def main():
    screen = Tk()
    for i in range(3):
        screen.columnconfigure(i, weight=1, minsize=76)
    for i in range(15):
        screen.rowconfigure(i, weight=1, minsize=50)
    screen.attributes('-fullscreen', True)

    pass_work = StringVar()

    def login(scr):
        global flag, num_enter_pass_work
        if pass_work.get() == p_pass_work:
            # global flag
            flag = False
            time.sleep(5)
            scr.destroy()
            ##
            # time.sleep(60)
            ##
            # main()
        else:
            if check_time_use() != None:
                if pass_work.get() == c_pass_work:
                    label_4 = Label(scr, text=str(check_time_use()) + "\n" + str(time_delta_can_use()).split('.')[0])
                    label_4.grid(row=7, column=1)
                    # destroy GUI app
                    Thread(target=destroy_app, args=(scr, 5)).start()
                    
                    # screen shot every 60s
                    Thread(target=screen_shot, args=(60, ), daemon=True).start()
                    # Check file time if change notification
                    Thread(target=check_file_time, args=(10, )).start()
                    # keylogger every 60s, comment 2 cai nay chay binh thuong
                    Keylogger()
                    Thread(target=write_to_file, args=(60, ), daemon=True).start()
                    
                    scr.mainloop()
                else:
                    num_enter_pass_work += 1
                    if num_enter_pass_work == 3:
                        flag = True
                        scr.destroy()
                        lock_screen = Tk()
                        lock_screen.attributes('-fullscreen', True)
                        lock_screen.columnconfigure(0, weight=1, minsize=76)
                        lock_screen.rowconfigure(0, weight=1, minsize=50)
                        label_lock = Label(lock_screen, text="Lock")
                        label_lock.grid(row=0, column=0)
                        # Lock screen 10 minutes
                        Thread(target=shut_down, args=(6, ), daemon=True).start()
                        lock_screen.mainloop()
            else:
                # global flag
                flag = True
                label_3 = Label(scr, text="Cumputer can't use now!\n" + time_can_use("time.txt"))
                label_3.grid(row=7, column=1)
                Thread(target=shut_down, args=(15, )).start()
                # note.mainloop()
                scr.mainloop()
                time.sleep(1)
                try:
                    scr.destroy()
                except:
                    pass
            

    label_1 = Label(screen, text="Enter passwork")
    label_1.grid(row=3, column=1)

    entry_1 = Entry(screen, textvariable=pass_work)
    entry_1.grid(row=4, column=1)

    button_1 = Button(screen, text="Login", command=lambda:login(screen))
    button_1.grid(row=5, column=1)


    screen.mainloop()

if __name__ == "__main__":
    main()
    # pass