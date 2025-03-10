#https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    res = gauge(percentage)
    if percentage:
        print( "Percentage:", res)    

def convert(fraction):
    try:
        x, y = fraction.split("/")
        percenage = round(( int(x) / int(y) ) * 100)

    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        return percenage  


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"




if __name__ == "__main__":
    main()