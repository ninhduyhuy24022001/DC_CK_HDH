from tkinter import *
from threading import Thread, local
import subprocess
import sys

from pass_work import get_pass_work
from Time import check_time_use
from Time import time_can_use
from Time import clock

flag = False
num_enter_pass_work = 0
p_pass_work, c_pass_work = get_pass_work("passwork.txt")


def shut_down(seconds):

    clock(seconds)
    global flag
    # print(flag)
    if flag:
        subprocess.Popen("shut_dow.bat")

# def 


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
            clock(2)
            scr.destroy()
            ##
            # time.sleep(60)
            ##
            # main()
        else:
            # note = Tk()
            # windowWidth = note.winfo_reqwidth()
            # windowHeight = note.winfo_reqheight()
        
            #     # Gets both half the screen width/height and window width/height
            # positionRight = int(note.winfo_screenwidth()/2 - windowWidth/2)
            # positionDown = int(note.winfo_screenheight()/2 - windowHeight/2)
        
            #     # Positions the window in the center of the page.
            # note.geometry("+{}+{}".format(positionRight, positionDown))
                
            if check_time_use():
                if pass_work.get() == c_pass_work:
                    pass
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
                        Thread(target=shut_down, args=(6, )).start()
                        lock_screen.mainloop()
            else:
                # global flag
                flag = True
                label_3 = Label(scr, text="Cumputer can't use now!\n" + time_can_use("time.txt"))
                label_3.grid(row=7, column=1)
                Thread(target=shut_down, args=(15, )).start()
                # note.mainloop()
                scr.mainloop()
                clock(1)
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