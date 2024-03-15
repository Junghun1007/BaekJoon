num = input()
num2 = 2 * int(num) - 1

null_num = list(map(abs,range(int(num)-1 ,-1 * int(num),-1)))

for i in null_num:
    for j in range(int(i)):
        print(" ",end="")
    for j in range(0,num2 - i*2):
        print("*",end="")
    print()
