word = input().strip()
cnt = 0
if word != "":
    for i in word:
        if i == " ":
            cnt += 1
    cnt += 1
print(cnt)