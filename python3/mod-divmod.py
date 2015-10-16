#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/python-mod-divmod

from __future__ import division
a = int(raw_input())
b = int(raw_input())

print(a//b)
print(a%b)
print(divmod(a,b))
