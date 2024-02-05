
num = int(input())
result = []
for c in range(0, num):
    input_text = input().split()
    count = int(input_text[0])
    text = input_text[1]
    word = ""
    for j in range(0,len(text)):
        for q in range(0,count):
            word = word + text[j]
    result.append(word)
for i in result:
    print(i)