
import math
print(math.radians(360))
print(math.radians(180))


import statistics
nlist1 = [1,2,3,4,5,6,7,8,9]
print(statistics.mean(nlist1))
print(statistics.median(nlist1))


import time
print(time.time())
start=time.time()
time.sleep(5)
end = time.time()
print("시간 차:",end-start)