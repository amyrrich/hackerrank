#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/exceptions

lines = int(input())

for i in range(lines):
  a,b = input().split()
  try:
    val = int(a)//int(b)
  except ZeroDivisionError as e:
    print ("Error Code:",e)
  except ValueError as e:
    print ("Error Code:",e)
  else:
    print(val)
