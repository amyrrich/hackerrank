#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/py-set-intersection-operation

numen = int(input())
subs = set(map(int,input().split()[:numen]))
numfr = int(input())
subs = subs.intersection(map(int,input().split()[:numfr]))
print(len(subs))
