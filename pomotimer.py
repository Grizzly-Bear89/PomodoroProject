import time



print("Would you like to start the timer?")
choice=input()
if choice == str("y"):
    print("is it a break or a working peroid?")
    choice2=input()
    if choice2 == str("break"):
        print("your five minute timer has started")
        for i in range(4):
             t = 5*60
             while t:
                 mins = t // 60 
                 secs = t % 60
                 timer = '{:02d} : {:02d}'.format(mins, secs)
                 print('' + timer, end="\r")
                 time.sleep(1)
                 t-=1
            print("Time to get back to work!!")
    else:
         print("you have started a pomodoro timer")
         for i in range(4):
             t = 25*60
             while t:
                 mins = t // 60 
                 secs = t % 60
                 timer = '{:02d} : {:02d}'.format(mins, secs)
                 print('' + timer, end="\r")
                 time.sleep(1)
                 t-=1
         print("Breaktime")


