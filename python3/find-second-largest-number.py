#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

listlen = int(input())
list = map(int,input().split())
list = sorted(set(list))
list.pop()
print(list.pop())
