
x = int(input())
nums = input().split()
y = int(input())

count = 0
for i in nums:
    if int(i) == y:
        count = count + 1
print(count)