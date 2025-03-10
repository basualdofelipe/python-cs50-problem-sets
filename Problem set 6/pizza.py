#https://cs50.harvard.edu/python/2022/psets/6/pizza/

from tabulate import tabulate
import csv, sys


def main():

    if len(sys.argv) > 2:
        print("Too many command-line arguments ")
    else:
        try:
            table = list(open_csv(f"csv/{sys.argv[1]}"))
        except IndexError:
            print("Missing command-line argument")
        except FileNotFoundError:
            print("Not a CSV file")
        else:
            print(tabulate(table, tablefmt="grid"))

def open_csv(file_path):
    with open(file_path) as file:
        reader = csv.reader(file)
        for name, small, large in reader:
            yield [name, small, large]

if __name__  == "__main__":
    main()

