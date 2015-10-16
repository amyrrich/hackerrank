#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/sets

firstnums = int(input())
firstset = set(map(int,input().split()[:firstnums]))
secondnums = int(input())
secondset = set(map(int,input().split()[:secondnums]))
newset = firstset.difference(secondset)
newset.update(secondset.difference(firstset))
newset = sorted(newset)
for i in range(len(newset)):
  print(newset[i])
