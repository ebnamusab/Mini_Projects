from datetime import datetime
import pytz

cities = pytz.all_timezones

city_name = input("Enter city name: ")

matching_tzone = [tZONE for tZONE in cities
                      if city_name.lower() in tZONE.lower()]

if not matching_tzone:
    print("No matching.")
else:
    if len(matching_tzone) > 1:
        print("Please choose one:")
        for idxNum, tZONE in enumerate(matching_tzone, start = 1):
            print(f"{idxNum}. {tZONE}")
        choice = int(input("Enter your choice: ")) - 1
        city_timezone = pytz.timezone(matching_tzone[choice])
    else:
        city_timezone = pytz.timezone(matching_tzone[0])

    city_time = datetime.now(city_timezone)

    print(city_time.strftime("Time is %I:%M %p and Date is %d-%b-%y"))
