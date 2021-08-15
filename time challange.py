import pytz
import datetime

available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Kolkata",
                   '3': "Australia/Adelaide",
                   '4': "Europe/Brussels",
                   '5': "Europe/London",
                   '6': "Japan",
                   '7': "Pacific/Tahiti",
                   '8': "US/Hawaii",
                   '9': "Zulu"}
print(input("Please select the zones and '0 to exite': "))
for place in sorted(available_zones):
    print("{} : {}".format(place, available_zones[place]))
while True:
    choice = input()
    if choice == 0:
        break
    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'),world_time.tzname()))
        # %A -Locale’s full weekday name.
        # %z Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM,
        # where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print()
