#https://cs50.harvard.edu/python/2022/psets/6/lines/

import sys


def main():
    if len(sys.argv) < 2:
        res = "Too few command-line arguments"
    elif len(sys.argv) > 2:
        res = "Too many command-line arguments"
    else:
        res = list(lines(sys.argv[1]))

    print(len(res))

def lines(py_file):
    try:
        with open(py_file) as file:
            for line in file:
                line = line.lstrip()
                if line.startswith("#") or line.startswith("\n") or line == "":
                    pass
                else:
                    yield line
    except FileNotFoundError:
        return "File does not exist"
    else:
        pass
    


if __name__ == "__main__":
    main()