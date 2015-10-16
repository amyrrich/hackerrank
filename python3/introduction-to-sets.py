#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/py-introduction-to-sets

i = int(input())
heights = set(int(x) for x in input().split()[:i])
print(sum(heights)/len(heights))
