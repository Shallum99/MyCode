ok = input().split()
li = []
for i in ok:
    li.append(i.swapcase())
print(*li[::-1])
