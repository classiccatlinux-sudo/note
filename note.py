import time
import os

#v1.1 will be the last :)

#boot
print("weclome to note a simple program for CLI sticky notes")
time.sleep(3)
os.system('clear')

#main
sticky1 = input("whats your sticky note? (press ctrl + c to stop): ")

os.system('clear')

print(sticky1)
try:
   while True:
       pass
except KeyboardInterrupt:
    pass
