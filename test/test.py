from datetime import datetime
from threading import Timer

def on_10th_second():
    print('yo-ho-ho', datetime.now())


def shedule(func, nth_sec):
    wait = 7200
    Timer(wait, func).start()
    Timer(wait + 1, lambda: shedule(func, nth_sec)).start()



shedule(on_10th_second, 10)

print('ok')



#center house:
#440 400


# start position house : 358 328


# offset x +82
# offset y +72
