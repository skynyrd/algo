#!/bin/python3

def time_conversion(s):
    time_in_array = s.split(":")
    hour = time_in_array[0]
    sym = time_in_array[2][-2:]

    if hour == "12" and sym.lower() == "am":
        hour = "00"
    elif sym.lower() == "pm":
        if hour != "12":
            new_hour = int(hour) + 12
            hour = str(new_hour)

    return hour + ":" + time_in_array[1] + ":" + time_in_array[2][:-2]


s = input().strip()
result = time_conversion(s)
print(result)
