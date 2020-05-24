'''
background: you are a bike shop. You rent bikes out to people every day, but you need to order the bikes in advance for a given day. As such, you need to know how many bikes will be used on any given day. However, if a bike is used in the morning for example, we can use it again in the evening (or whenever it is returned to the shop)

input: list of times bikes are checked out from
output: how many bikes we need for that given day
           s1 f1  s2  f2
example: [[8,11], [15,16]]
output: 1
           s1 f1   s2 f2
example: [[8,11], [10,16]]
output: 2

example: [[8,11],[9,10],[10,16]]
8    11
 9 10
   10     16
   
   
output: 2

            0     1     2      3    4
example: [[1,5],[2,4],[3,9],[4,8],[5,11]]

[1,5][5,11]
[2,4][4,8]
[3,9]
Run: O(N*logN) 
Space: O(N)
minheap [4,5,9]
si+1 =< fi add(fi+1)
si+1 =< minheap[0] add(fi+1)
2 < 5 add(4)
3 < 4 add(9)
4 = 4 remove(4) add(fi+1) [5,8,9]
5 = 5 remove(5) add(fi+1) [8,9,11]

ouput: 3
'''

import heapq

def foo(arr):
    pq = []
    for s in arr:
        if len(pq) > 0 and s[0] >= pq[0]:
            heapq.heapreplace(pq,s[1])
        else:
            heapq.heappush(pq,s[1])
            
    return len(pq)

print(foo([[8,11], [15,16]]))
print(foo([[8,11], [10,16]]))
print(foo([[8,11],[9,10],[10,16]]))
print(foo([[1,5],[2,4],[3,9],[4,8],[5,11]]))
