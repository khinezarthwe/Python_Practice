#Challenge 6
#Write a program that converts text written numbers (Ex: Thirty-One) to its numeric form (Ex: 31)
# and perform the opposite. Input: 31 Output: (Thirty-One)
from word2number import w2n
from num2words import num2words

print(num2words(42))
print(w2n.word_to_num('112'))
print(w2n.word_to_num('point one'))

print(num2words(100))
