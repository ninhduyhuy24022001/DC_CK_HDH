import os
from Time import to_day


# if not os.path.exists(to_day()):
#     os.makedirs(to_day())

path = to_day() + '\\screen_shot'
print(os.path.exists(path))
if not os.path.exists(path):
    os.makedirs(path)

# with open("t.txt" , 'w', encoding='utf8') as f:
#     text = "\x03"
#     f.write(text)