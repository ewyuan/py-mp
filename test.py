import time
import sys
for i in range(100):
    time.sleep(1)
    sys.stdout.write("\r%d%%" % i)
    sys.stdout.flush()