import time
import os

#boot
print("loading...")
time.sleep(4)
print("weclome to note a simple program for CLI sticky notes")
time.sleep(4)
os.system('clear')

#main
sticky1 = input("whats your sticky note? (press ctrl + c to stop):")

os.system('clear')

print(sticky1)
try:
   while True:
       pass
except KeyboardInterrupt:
    pass

