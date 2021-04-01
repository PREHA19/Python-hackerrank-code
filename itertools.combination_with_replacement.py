from itertools import combinations_with_replacement
a,b=input().split()
b=int(b)
lst1=list(combinations_with_replacement(sorted(a),b))

for i in lst1:
   
    print(*[''.join (i)])
