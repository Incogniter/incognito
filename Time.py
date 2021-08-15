import time
time_here = time.localtime()
print("Date:", time_here.tm_year, ":", time_here.tm_mon, ":", time_here.tm_mday)
print("Time:", time_here.tm_hour, ":", time_here.tm_min, ":", time_here.tm_sec)
print("_"*50)
from time import time as my_timer
import random
input("Press enter to START")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to STOP")

end_time = my_timer()
print("Started at " + time.strftime("%X", time.localtime(start_time)))
# The strftime() method returns a string representing date and time using date, time or datetime object.
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
# strftime() contain many format codes for ex %X and %x
# %x is to print date and %X is to print time
print("Your reaction timer is {}".format(end_time - start_time))
