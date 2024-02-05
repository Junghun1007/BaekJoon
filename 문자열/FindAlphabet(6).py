word = list(input())
num_list = [-1 for i in range(0,26)]

for i in word:
    n = ord(i) - 97
    num_list[n] = word.index(i)


for w in num_list:
    print(w,end=" ")