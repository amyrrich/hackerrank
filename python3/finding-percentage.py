#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/finding-the-percentage

Students = dict()
Total = 0.0

for i in range(int(input())):
  Entries = input().split()
  Name = Entries[0]
  Entries.remove(Entries[0])
  Students[Name] = Entries

Query = input()
if (Query in Students):
  NumGrades = len(Students[Query])
  for Grades in range(NumGrades):
    Total += float(Students[Query][Grades])
  Total = Total/NumGrades
  print("%.2f" % Total)
