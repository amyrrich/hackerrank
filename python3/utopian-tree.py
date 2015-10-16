#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/utopian-tree

for test in (range(int(input()))):
  cycles = int(input())
  height = 1
  for i in (range(cycles)):
    if cycles == 0:
      height = 1
    if i%2 != 0:
      height += 1
    else:
      height *= 2
  print(height)
