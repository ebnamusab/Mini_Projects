from datetime import datetime
import pytz

cities = pytz.all_timezones
print(cities)

city_name = input("Enter city name: ")

country_name = pytz.timezone(city_name)
country_time = datetime.now(country_name)
print(country_time.strftime("Time is %I:%M %P and Date is %d-%b-%y"))