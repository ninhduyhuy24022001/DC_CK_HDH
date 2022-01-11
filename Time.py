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
            return i
    return None

def time_can_use(file_path):
    with open(file_path) as f:
        time_use = ""
        for line in f.readlines():
            time_use += line
    return time_use

def time_delta_can_use():
    t = check_time_use()
    today  = datetime.datetime.now()
    if check_time_use != None:
        return (t['T'] - today)
    return  None

def next_time():
    t = check_time_use()
    list_time = get_list_time("time.txt")
    minn = datetime.timedelta(seconds=100000)
    h = None
    for i in list_time:
        # print(i["F"] - t["T"])
        if i["F"] - t["T"] < minn and i["F"] - t["T"] > datetime.timedelta(seconds=0):
            minn = (i["F"] - t["T"])
            h = i
    return h
    
def time_now():
    now = datetime.datetime.now()
    return now.strftime("%Y_%m_%d-%H_%M")

def to_day():
    now = datetime.datetime.now()
    return now.strftime("%Y_%m_%d")

if __name__ == "__main__":
    t = time_delta_can_use() <= datetime.timedelta(seconds=60)
    print(t)
