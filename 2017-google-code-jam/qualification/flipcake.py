import numpy as np
def flipcake(s,k):
    if len(s)<k:
        return -1

    # convert string s to bool
    bs = np.asarray([0 if ele=='-' else 1 for ele in s])
    cnt = 0
    for i in range(len(bs)):
        if(i==len(bs)-k):
            if(all(bs[i:])):
                break
            elif all(1-bs[i:]):
                cnt +=1
                break
            else:
                return -1

        if bs[i]==0:
            bs[i:i+k] = 1-bs[i:i+k]
            cnt += 1

    return cnt

#f = open('A-small-practice.in')
#lines = [ele for ele in f]
#s = lines[0]
s = raw_input()
t = int(s)
for i in xrange(1, t+1):
    line = raw_input()
    s, t = line.split(' ')
    rst  = flipcake(s, int(t))
    rst = 'IMPOSSIBLE' if rst < 0 else str(rst)
    print "Case #{}: {}".format(i, rst)


