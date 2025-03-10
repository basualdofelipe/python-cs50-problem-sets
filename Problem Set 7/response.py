#https://cs50.harvard.edu/python/2022/psets/7/response/

import validators


def main():
    print(validate(input("What's your email address?: ")))


def validate(mail):
    return "Valid" if validators.email(mail) else "Invalid"


if __name__ == "__main__":
    main()