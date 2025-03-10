#https://cs50.harvard.edu/python/2022/psets/8/seasons/

from datetime import date, datetime
import inflect, sys

p = inflect.engine()

def main():
    minutes = calc_minutes(input("Date of Birth: "))
    print(minutes)

def calc_minutes(birth_date, today=date.today()):
    try:
        birth = datetime.strptime(birth_date, "%Y-%m-%d").date()
    except Exception:
        sys.exit("Ivalid date")
    else:
        return p.number_to_words((today - birth).days * 1440).capitalize() + " minutes"



if __name__ == "__main__":
    main()