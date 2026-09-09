import time
import threading
def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")
def drink_coffee():
    time.sleep(4)
    print("you drank coffee")
def study():
    time.sleep(5)
    print("you finish studying")

x=threading.Thread(target=eat_breakfast) 
x.start() 
y=threading.Thread(target=drink_coffee)
y.start()
z=threading.Thread(target=study)
z.start()

x.join() 
y.join()
z.join()

print(threading.active_count()) 
print(threading.enumerate())    
print(time.perf_counter()) 