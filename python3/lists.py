#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/python-lists

List = []
for i in range(int(input())):
  Actions = input().split()
  Command = Actions[0]
  Actions.remove(Actions[0])
  Actions = [int(n) for n in Actions]
  if Command == "print":
    print(List)
  else:
    getattr(List, Command)(*Actions)
