#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/sets

numen = int(input())
subs = set(map(int,input().split()[:numen]))
numfr = int(input())
subs = subs.symmetric_difference(map(int,input().split()[:numfr]))
print(len(subs))
