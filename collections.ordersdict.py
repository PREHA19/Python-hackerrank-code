from collections import OrderedDict
n=int(input())
od = OrderedDict()
for i in range(n):
    
    item_name,_,price = input().rpartition(" ")
    if item_name in od.keys():
        od[item_name]= od[item_name] + int(price)
    else:
        od[item_name]= int(price)
for item_name,net_price in od.items():
    print(item_name,net_price)
