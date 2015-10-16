#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/python-mutations

str = list(input())
index,replace = input().split()
index = int(index)
str[index] = replace
str = ''.join(str)
print(str)

