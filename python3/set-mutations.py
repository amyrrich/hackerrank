#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/py-set-mutations

setlen = int(input())
setnums = set(map(int,input().split()[:setlen]))
for i in range(int(input())):
  command,newsetlen = input().split()
  newset = set(map(int,input().split()[:int(newsetlen)]))
  getattr(setnums, command)(newset)
print(sum(setnums))
