#https://cs50.harvard.edu/python/2022/psets/5/test_plates/


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #No periods, spaces, or punctuation marks are allowed.
    for i in s:
        if i in ",.-;:_+' ":
            return False

    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if 6 < len(s) or len(s) < 2:
        return False
    
    # All vanity plates must start with at least two letters.
    if  s[0].isdigit() or s[1].isdigit():
        return False
            
    #Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    #The first number used cannot be a '0'.
    x = []
    for i in s:
        if i.isdigit():
            x.append(i)
            # VVVVV if there is a letter at the end it returns False
            if not s[-1].isdigit():
                return False
    if x[0] == '0':
        return False
    
    else:
        return True


if __name__ == "__main__":
    main()