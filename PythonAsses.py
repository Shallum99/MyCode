# Question:
# To take an input(string) from the user and swap the case of that string and return the reverse of that string.
# Sample case 0:
# Input:
# rUn DoGs
# Output:
# dOgS RuN


ok = input().split()
li = []
for i in ok:
    li.append(i.swapcase())
print(*li[::-1])
