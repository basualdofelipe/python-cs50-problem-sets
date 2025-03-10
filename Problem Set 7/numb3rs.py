#https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if re.search(r"^(?:(?:1\d{2}|2[0-4]\d|25[0-5]|\d{1,2})\.){3}(?:1\d{2}|2[0-4]\d|25[0-5]|\d{1,2})$",ip):
        return True
    else:
        return False
    
#the next function is just another way but with easier redex and checking with a loop if each number is less than 256
def validate_2(ip):

    if matches := re.search(r"^(\d{1,3}\.){3}(\d{1,3})$",ip):
        for number in matches.group(0).split("."):
            print(number)
            if int(number) > 255:
                return False
        return True    
    else:
        return False



if __name__ == "__main__":
    main()