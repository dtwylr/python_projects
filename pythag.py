#! usr/local/bin/python3
import time
total = 1000
t0 = time.time()
for a in range(1,total):
    for b in range(1,total):
        c = total-a-b
        if (a**2+b**2-c**2 == 0):
            print(a,b,c)
            print(a*b*c)
            break
t1 = time.time()
print('operation took',t1-t0,'seconds')
