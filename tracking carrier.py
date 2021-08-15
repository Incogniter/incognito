import phonenumbers

number = input("Enter the number with country code:")
from phonenumbers import geocoder
ch_number =phonenumbers.parse(number,"CH")
#CH-contryhistory
print(geocoder.description_for_number(ch_number,"en"))
from phonenumbers import timezone
timezone = timezone.time_zones_for_number(ch_number)
print(timezone)
from phonenumbers import carrier
service_provider = phonenumbers.parse(number,"CH")
print(carrier.name_for_number(service_provider,"en"))