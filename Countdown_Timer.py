import time
import winsound
t = int(input("Enter the CountDown Duration: "))
def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        winsound.Beep(1000,150)
        print(timer, end="\r")
        time.sleep(1)
        
        t -= 1
    print("Time's up!")
    if t == 0:
       winsound.Beep(2500,800)
       
countdown(t)