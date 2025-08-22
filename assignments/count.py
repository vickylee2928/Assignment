"""
BOMB COUNTDOWN TIMER
This program counts down from 10 to 1 with a 1-second delay between numbers.
"""


import time

count = 10 
print("COUNTDOWN STARTED!")

while count > 0:
    print(f"{count}")
    time.sleep(1)
    count -= 1

print("BOOM!")    