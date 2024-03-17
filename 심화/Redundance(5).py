word = input().lower()
word_alp = list(set(list(word)))
word = list(word)
cnt = [0 for i in range(len(word_alp))]
def count_redundancy(input_num, input_list):
    cnt1 = 0
    for i in input_list:
        if i == input_num:
            cnt1 += 1
    if cnt1 >= 2:
        return 0

for wa in word_alp:
    for w in word:
        if wa == w:
            cnt[list(word_alp).index(wa)] += 1

if count_redundancy(max(cnt),cnt) == 0:
    print("?")
else:
    print(word_alp[cnt.index(max(cnt))].upper())

print(word_alp)
print(cnt)

