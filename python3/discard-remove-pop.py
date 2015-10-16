#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/py-set-discard-remove-pop

n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
  actions = input().split()
  command = actions[0]
  if command == "pop":
    s.pop()
  else:
    getattr(s, command)(int(actions[1]))
print(sum(s))
