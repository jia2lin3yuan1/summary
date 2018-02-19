import numpy as np
import heapq
from collections import defaultdict
def selectStall(numS, numP):
    if numP == numS:
        return 0, 0
    hq = []
    dt = defaultdict()
    heapq.heappush(hq, -numS)
    dt[numS] = 1
    while(numP > 0):
        ele   = -(heapq.heappop(hq))
        cnt   = dt[ele]
        numP -= cnt
        del dt[ele]

        minV = (ele -1)//2
        maxV = ele - 1 - minV
        if minV > 0:
            if minV in dt.keys():
                dt[minV] += cnt
            else:
                heapq.heappush(hq, -minV)
                dt[minV] = cnt
        if maxV > 0:
            if maxV in dt.keys():
                dt[maxV] += cnt
            else:
                heapq.heappush(hq, -maxV)
                dt[maxV] = cnt

    return minV, maxV

def selectStall2(numS, numP):
    if numP == numS:
        return 0, 0
    arr = np.asarray([numS])
    while(numP > arr.shape[0]):
        numP -= arr.shape[0]
        hf_min = (arr-1)//2
        hf_max = (arr-1)-hf_min
        min_indices = np.where(hf_min>0)[0]
        max_indices = np.where(hf_max>0)[0]
        arr = np.concatenate((hf_max[max_indices], hf_min[min_indices]))

    hq = []
    for k in range(arr.shape[0]):
        heapq.heappush(hq, -arr[k])
    while True:
        ele = -(heapq.heappop(hq))
        minV = (ele-1)//2
        maxV = (ele-1) - minV
        numP -= 1
        if(numP == 0):
            break
        else:
            if(minV > 0):
                heapq.heappush(hq, -minV)
                heapq.heappush(hq, -maxV)
            elif(maxV > 0):
                heapq.heappush(hq, -maxV)

    return minV, maxV

s = raw_input()
t = int(s)
for i in xrange(1, t+1):
    line = raw_input()
    s,k = line.split(' ')
    minV, maxV = selectStall(int(s),int(k))
    print "Case #{}: {} {}".format(i, maxV, minV)

