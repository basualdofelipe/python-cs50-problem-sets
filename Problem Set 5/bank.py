#https://cs50.harvard.edu/python/2022/psets/5/test_bank/

def main():
    greeting = input("Hello\n").lower()
    cash = value(greeting)
    print("$", cash, sep="")


def value(greeting):
    if greeting == "": return 100 #so it does no't give index error, in problem set 1 I can't use "try"

    if greeting == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
