#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/a-very-big-sum

total = 0
numints = int(input())
nums = input()
while numints > 0:
    numints -= 1
    total += int(nums.split()[numints])
print(total)
