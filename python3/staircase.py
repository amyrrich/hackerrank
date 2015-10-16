#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/staircase

numberOfLines = int(input())
totalLines = numberOfLines
while numberOfLines > 0:
    numberOfLines -= 1
    for x in range(0, numberOfLines):
        print (" ", end="")
    for x in range(numberOfLines, totalLines):
        print ("#", end="")
    print()
