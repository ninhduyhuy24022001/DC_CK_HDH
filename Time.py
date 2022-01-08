import datetime
import time

def get_list_time(file_path):
    today = datetime.datetime.now()
    with open(file_path) as f:
        result = []
        for line in f.readlines():
            element_line = line.strip("\n").split()
            dic = {}
            for e in element_line:
               dic[e[0]] = e[1:]

            for k in dic:
                if k == 'F' or k == 'T':
                    dic[k] = datetime.datetime.strptime(str(today.date()) + " " + dic[k], "%Y-%m-%d %H:%M")
                else:
                    dic[k] = datetime.timedelta(minutes=int(dic[k]))
            result.append(dic)

    return result


def check_time_use():
    today = datetime.datetime.now()
    list_time = get_list_time("time.txt")
    for i in list_time:
        if today >= i['F'] and today < i['T']:
            return True
    return False

def time_can_use(file_path):
    with open(file_path) as f:
        time_use = ""
        for line in f.readlines():
            time_use += line
    return time_use
    
def clock(seconds):
    time.sleep(seconds)
    return 0

if __name__ == "__main__":
    t = time_can_use("time.txt")
    print(t)