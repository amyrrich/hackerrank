#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/the-minion-game

word = input()
strln = len(word)
sublen = strln
consonants = 0
vowels = 0

for i in range(strln):
  if word[i] in 'AEIOU':
    vowels += sublen
  else:
    consonants += sublen
  sublen -= 1
if consonants > vowels:
  print("Stuart %d" % consonants)
elif vowels > consonants:
  print("Kevin %d" % vowels)
else:
  print("Draw")
