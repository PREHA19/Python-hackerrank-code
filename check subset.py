t=int(raw_input())

for i in (range(0,t)):
    a=raw_input()
    lst1=set(raw_input().split())
    b=raw_input()
    lst2=set(raw_input().split())
    lst3=lst1.intersection(lst2)
    if lst3==lst1:
        print ("True")
    else:
        print ("False")    
