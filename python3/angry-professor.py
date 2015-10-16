#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/angry-professor

NumClasses = int(input())

while NumClasses > 0:
  OntimeStudents = 0
  NumStudents, CancelThreshold = map(int, input().split())
  Arrivals = input()

  while NumStudents > 0:
    if int(Arrivals.split()[NumStudents-1]) <= 0:
      OntimeStudents += 1
    NumStudents -= 1
  if OntimeStudents >= CancelThreshold:
    print("NO")
  else:
    print("YES")
  NumClasses -= 1
