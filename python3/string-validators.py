#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/string-validators

str = list(input())
hasalnum = hasal = hasdig = hasup = haslo = 'False'
for i in range(len(str)):
  if str[i].isalpha():
    hasal = 'True'
    hasalnum = 'True'
    if str[i].islower():
      haslo = 'True'
    if str[i].isupper():
      hasup = 'True'
  if str[i].isdigit():
    hasdig = 'True'
    hasalnum = 'True'
print(hasalnum)
print(hasal)
print(hasdig)
print(haslo)    
print(hasup)
