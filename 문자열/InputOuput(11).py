word = []
while True:
    try:
        line = input()
        if line == "":
            break
        word.append(line)
    except EOFError:
        break

for i in word:
    print(i)