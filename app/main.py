import os
import sys
import time

while True:
    time.sleep(5)
    greeting = os.environ.get("GREETING")
    print(greeting)
    sys.stdout.flush()
