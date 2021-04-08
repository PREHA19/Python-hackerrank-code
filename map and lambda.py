cube = lambda x:x*x*x

def fibonacci(n):
    l=list()
    if n==0:
        pass
    elif n==1:
        l.append(0)
    elif n==2:
        l.append(0)
        l.append(1)
    elif n==3:  
        l.append(0)
        l.append(1)  
        l.append(1)
    else:
        a=0
        l.append(a)
        b=1
        l.append(b)
        c=1
        l.append(c)
    
    for i in range(2,n-1):
        d=b+c
        l.append(d)
        b=c
        c=d
        
    return l
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
