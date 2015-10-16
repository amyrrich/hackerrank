#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/plus-minus

numdig = int(input())
divisor = numdig
negative = 0
positive = 0
zeronum = 0
nums = input()
while numdig > 0:
    numdig -= 1
    num = int(nums.split()[numdig])
    if num < 0:
        negative += 1
    elif num > 0:
        positive += 1
    else:
        zeronum += 1
print ("{0:.3f}".format(positive/divisor))
print ("{0:.3f}".format(negative/divisor))
print ("{0:.3f}".format(zeronum/divisor))
