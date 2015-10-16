#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/solve-me-second

def solveMeSecond(a,b):
   return a+b
n = int(input())
for i in range(0,n):
    a, b = map (int,input().split())
    res = solveMeSecond(a,b)
    print (res)
