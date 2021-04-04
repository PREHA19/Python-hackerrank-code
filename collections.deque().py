from collections import deque
d = deque()
n=int(input())
for i in range(n):
    m=input().split()
    if m[0]=='append':
        d.append(m[1])
    elif m[0]=='appendleft':
        d.appendleft(m[1])
    elif m[0]=='pop':
        d.pop()  
    else:
        d.popleft()   
print(*d)    
