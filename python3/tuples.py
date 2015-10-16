#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/python-tuples

Nums = int(input())
NumTuple = tuple(map(int,input().split()[:Nums]))
print (hash(NumTuple))
