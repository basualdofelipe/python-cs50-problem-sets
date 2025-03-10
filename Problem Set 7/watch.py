#https://cs50.harvard.edu/python/2022/psets/7/watch/

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r".+src=\"https?://www.youtube.com/embed/([^\"]+).+",s):
        return "https://youtu.be/" +  matches.group(1)
    else:
        return None



if __name__ == "__main__":
    main()