#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/py-set-add

countries = set()
for i in range(int(input())):
  countries.add(input())
print(len(countries))
