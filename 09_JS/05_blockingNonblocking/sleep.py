from time import sleep


def sleep_3s():
    sleep(3)
    print("wakeup!")


print("start sleeping")
sleep_3s()
print("End of program")
