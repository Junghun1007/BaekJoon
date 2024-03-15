chess = [1, 1, 2, 2, 2, 8]
input_num = input().split()
result = []
for i in range(6):
    chess[i] = chess[i] - int(input_num[i])

for i in chess:
    print(i, end=" ")