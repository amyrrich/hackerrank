#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/diagonal-difference

rightpos = int(input())
leftpos = 0
firstdiag = 0
seconddiag = 0
while rightpos > 0:
    # Type below...
    nums = input()
    firstdiag += int(nums.split()[leftpos])
    leftpos += 1
    rightpos -= 1
    seconddiag += int(nums.split()[rightpos])
if (firstdiag <= 0):
    if (seconddiag <= 0):
        diff = abs(firstdiag - seconddiag)
    else:
        diff = abs(firstdiag) + seconddiag
else:
    if (seconddiag <= 0):
        diff = firstdiag - seconddiag
    else:
        diff = abs(firstdiag - seconddiag)
print(diff)
                    
