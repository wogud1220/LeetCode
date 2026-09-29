word1 = input()
word2 = input()

# Please write your code here.

word1, word2 = list(word1), list(word2)
word1.sort()
word2.sort()

if len(word1) == len(word2) and word1 == word2:
    print("Yes")
else:
    print("No")