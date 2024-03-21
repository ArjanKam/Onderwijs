from time import sleep

print("Start Programma")

def doProcess():
    print("blablabla")
    sleep(10)
    print("blablabla")
    print("blablabla")
    print("blablabla")
    print("blablabla")
    print("blablabla")

counter = 0
while True:
    
    sleep(1)
    print(".", end="")
    counter += 1
    
    if counter % 10 == 0:
        print()
        print("10 seconden later")
        doProcess()
