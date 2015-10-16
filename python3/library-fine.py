#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/library-fine

ActualDay, ActualMonth, ActualYear = map(int, input().split())
ExpectedDay, ExpectedMonth, ExpectedYear = map(int, input().split())

if ActualYear <= ExpectedYear:
  if ActualYear < ExpectedYear:
      fine = 0
  elif ActualMonth < ExpectedMonth:
    fine = 0
  elif ActualMonth > ExpectedMonth:
    fine = 500 * (ActualMonth - ExpectedMonth)
  else:
    if ActualDay < ExpectedDay:
      fine = 0
    else:
      fine = 15 * (ActualDay - ExpectedDay)
else:
  fine = 10000      
print(fine)

