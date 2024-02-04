
x = int(input())
result = []
for i in range(0,x):
    word = input()
    word = word[0] + word[-1]
    result.append(word)

for i in result:
    print(i)

