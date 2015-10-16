#!/opt/local/bin/python3.4

# https://www.hackerrank.com/challenges/time-conversion

time = input()
hour = int(time.split(":")[0])
minute = int(time.split(":")[1])
rest = time.split(":")[2]
second = int(rest[0:2])
ampm = rest[2:4]
ampm.upper()
if 'PM' in ampm:
    if hour < 12:
        hour += 12
else:
    if hour > 11:
        hour = 0
print("%02d:%02d:%02d" % (hour, minute, second))
