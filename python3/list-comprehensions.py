#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/list-comprehensions

x = int(input())
y = int(input())
z = int(input())
n = int(input())
lst = []

for i in range (x+1):
  for j in range (y+1):
    for k in range (z+1):
      if i+j+k != n:
        lst += [[i,j,k]]
print(lst)
