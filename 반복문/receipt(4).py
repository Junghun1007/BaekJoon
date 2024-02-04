

price = int(input())
count = int(input())
result = 0
for i in range(0,count):
    x, y = [int(j) for j in input().split()]
    result = (x * y) + result

if price == result:
    print("Yes")
else:
    print("No")









