# Question:
# To take an input(string) from the user and swap the case of that string and return the reverse of that string.
# Sample case 0:
# Input:
# rUn DoGs
# Output:
# dOgS RuN


li = [i.swapcase() for i in input().split()]
print(*li[::-1])
