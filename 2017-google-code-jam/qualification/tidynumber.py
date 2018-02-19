def tidy_number(data):
    # extract string from data on base of 10.
    sdata   = [data%10]
    data    = data/10
    keepNum = 1
    while data > 0:
        modV = data % 10
        data = data / 10
        if(modV > sdata[0]):
            sdata[0] = 9
            sdata    = [modV -1] + sdata
            keepNum  = 1
        else:
            sdata    = [modV] + sdata
            keepNum += 1

    # remove leading 0
    while(sdata[0] == 0 and keepNum > 0):
        del sdata[0]
        keepNum -= 1

    tidyInt = 0
    for i in range(keepNum):
        tidyInt = tidyInt*10 + sdata[i]
    for i in range(keepNum, len(sdata)):
        tidyInt = tidyInt*10 + 9

    return tidyInt

s = raw_input()
t = int(s)
for i in xrange(1, t+1):
    line = raw_input()
    tidy_int = tidy_number(int(line))
    print "Case #{}: {}".format(i, tidy_int)

