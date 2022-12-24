import time
def countDown_timer(seconds):
    while seconds>0:
     mins=int(seconds/60)
     sec=int(seconds%60)
     timer = f'{mins}:{sec}'
     print(timer)
     seconds-=1
    print('time up')
    
seconds=input('enter the time in number of seconds')
countDown_timer(int(seconds))