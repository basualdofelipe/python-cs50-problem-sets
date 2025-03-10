#https://cs50.harvard.edu/python/2022/psets/7/working/

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"(\d{1,2}):?(\d{1,2})? (AM|PM) (?:to) (\d{1,2}):?(\d{1,2})? (AM|PM)",s):
        first_hour = convert_meridiem(*matches.groups()[0:3])
        second_hour = convert_meridiem(*matches.groups()[3:6])
        return f"{first_hour} to {second_hour}"
    
    else:
        raise ValueError("input not accepted")



def convert_meridiem(hour, minute, meridiem):
    hour = int(hour)
    minute = int(minute) if minute != None else 0
    
    if meridiem == "AM":
        pass
    else:
        hour += 12
    
    return f"{hour:02d}:{minute:02d}"


if __name__ == "__main__":
    main()