from itertools import combinations
a,b=input().split()
b=int(b)
c=sorted(a)
for i in range(1,b+1):
    
    d=list(combinations(c,i)) 

    for j in d:
        print(*["".join(j)])
