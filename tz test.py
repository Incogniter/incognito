import pytz
import datetime

country = 'Asia/Kolkata'
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
# Use the datetime. datetime. now() to get the current date and time
# tz - Retrieve a time zone object from a string representation
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))
# utcnow to return utc date
# UTC = Coordinated Universal Time

print("_" * 50)
# for x in pytz.all_timezones:
#     print(x)
# print("_"*50)
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])
# print("="*50)
# for x in sorted(pytz.country_names):
#     print("{}:{}:{}".format(x , pytz.country_names[x], pytz.country_timezones.get(x)))

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=':')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")
