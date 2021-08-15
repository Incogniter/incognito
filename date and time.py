import time

print("The epoch on this system started at", time.strftime('%c', time.gmtime()))
# %c - Locale’s appropriate date and time representation.    #""".gmttime"""== UTC time
# UTC = Coordinated Universal Time
# print("The current timezone is {} with an offset of {}".format(time.tzname,time.timezone))
# OUTPUT WILL BE :The current timezone is ('India Standard Time', 'India Daylight Time') with an offset of -19800
print("The current timezone is {} with an offset of {}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("Day light saving time is in effect for this location")
    print("The DTS timezone is " + time.tzname[1])

print("Local time is " + time.strftime("%Y-%m-%d || %H:%M:%S", time.localtime()))
print("UTC time is " + time.strftime("%Y-%m-%d || %H:%M:%S", time.gmtime()))
# %Y - Year with century as a decimal number eg:2001.
# %m - Month as a decimal number [01,12]
# %d - Day of the month as a decimal number [01,31].
# %H - Hour (24-hour clock) as a decimal number [00,23]
# %M - Minute as a decimal number [00,59].
# %S - Second as a decimal number [00,61].


