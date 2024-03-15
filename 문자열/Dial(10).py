word = list(input())
alp = ["ABC", "DEF", "GHI", "JKL","MNO", "PQRS", "TUV","WXYZ"]
result = 0
for i in word:
    for j in alp:
        a = list(j)
        if i in a:
            result = alp.index(j) + result + 3

print(result)