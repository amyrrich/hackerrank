#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/simple-array-sum

total = 0
numints = int(input())
nums = input()
while numints > 0:
    numints = numints - 1
    total += int(nums.split()[numints])
print (total)
