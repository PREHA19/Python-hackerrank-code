from collections import Counter
number_of_shoes = int(input())
sizes_in_stock = Counter(map(int, input().split()))

total_revenue = 0
m=int(input())
for _ in range(m):
    size, price = map(int, input().split())
    if sizes_in_stock[size]:
        total_revenue += price
        sizes_in_stock[size] -= 1

print(total_revenue)
