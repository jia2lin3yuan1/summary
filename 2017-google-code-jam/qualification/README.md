
## BathStall:
The first solution coming to my mind is:
+ create two lists, they are used to record Ls and Rs for each stall respectively.
+ each time one person enters, find the stall 'S' with maximum min(Ls, Rs) and maximum max(Rs, Ls) if there are multiple available stalls under condition 1.
+ update Rs aheading of 'S', and Ls which are after 'S'.
+ Repeat entering persons until the last one.
+ <span style="color:red">It is not efficient in case the number of stalls is huge. The excuting time for small test case 2 and the large test is too long.</span>

The second solution is:
+ <span style="color:blue">Idea: There would be lots of continuous available stalls after several persons are in the stalls. Each time entering one person, select the maximum continous available stalls, and the person take the middle one.<span>
+ create an array to record the length of each continuous available stalls.
+ when length of array is shorter than left number of persons, all continuous stalls would have one person entering.
+ when length of array is longer than left number of persons, sort the array in decreasing order. the Previous (the left number of person -1) continuous stalls would be taken. Sort the length all continuous stalls.
+ Then only one person left, select the largest continuous stalls, the person enters the middle stall and compute min(Ls, Rs) as the smallest half size, max(Ls, Rs) as the largest half size.
+ <span style="color:red">It's about 50x faster than the Method 1, but it still not efficient on the large test case.<span>

The third solution is making use of dictionary and a priority queue.
+ <span style="color:blue">Idea: the priority queue is used to record the length of continuous available stalls. The dictionary record the counting number of one specific length of continuous stalls.<span>
+ Initial state: priority queue has one element, it's the number of stalls. The dictionary has key 'number of stall' with value '1'.
+ When there are still persons waiting to enter the stall, find the maximum length of continuous stall, count persons enter the middle stall.
+ <span style="color:red">It's 100x faster than the Method 2. It's pretty efficient.<span>
