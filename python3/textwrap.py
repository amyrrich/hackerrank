#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/text-wrap

import textwrap
str = input()
max = int(input())

print(textwrap.fill(str,max))
