import pytz
import datetime

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive utc time {}".format(utc_time))

# localize() is the correct function to use for creating datetime aware objects with an initial fixed datetime value.
aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware utc time {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))

print()

gap_time = datetime.datetime(2001, 6, 28, 12, 15, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 993710700
t = s +(60 * 60)


gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))
