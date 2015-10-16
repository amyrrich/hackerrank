#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/python-power-mod-power

a,b,m = int(raw_input()),int(raw_input()),int(raw_input())
print(pow(a,b))
if b >= 0:
  print(pow(a,b,m))
else:
  print("b cannot be negative")
