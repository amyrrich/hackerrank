#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/py-set-union

numen = int(input())
subs = set(map(int,input().split()[:numen]))
numfr = int(input())
subs = subs.union(map(int,input().split()[:numfr]))
print(len(subs))
