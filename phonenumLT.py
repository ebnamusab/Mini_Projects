import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter Your Number Here: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
# time_1 = timezone.time_zones_for_geographical_number(phone)
sim_details = carrier.name_for_number(phone, "en")
register = geocoder.description_for_number(phone, "en")

print(number)
print(phone)
print(time)
# print(time_1)
print(sim_details)
print(register)