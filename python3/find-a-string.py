#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/find-a-string

str = input()
substr = input()
index = 0
count = 0
for i in range(len(substr),len(str)+1):
  if substr in str[index:i]:
    count += 1
  index += 1
print(count)
