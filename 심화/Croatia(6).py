croatia = ["c=", "c-","dz=","d-","lj","nj","s=","z="]

word = input()
cnt = 0
for w in croatia:
    cnt += word.count(w)
    word = word.replace(w, ' ', word.count(w))
word = word.replace(' ','',len(word))
cnt += len(word)
print(cnt)

