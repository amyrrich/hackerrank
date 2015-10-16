#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/py-set-difference-operation

numen = int(input())
subs = set(map(int,input().split()[:numen]))
numfr = int(input())
subs = subs.difference(map(int,input().split()[:numfr]))
print(len(subs))
