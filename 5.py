num = int(input())
a = set()
for i in range(num):
    word = input()
    if 'Не' in word[0:3] or 'не' in word[0:3]:
        word = word[3:]
    a.add(word)
for i in a:
    print(i)
