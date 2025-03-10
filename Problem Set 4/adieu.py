# https://cs50.harvard.edu/python/2022/psets/4/adieu/

import inflect

p = inflect.engine()

def main():
    name_list = []
    while True:
        try:
            name_list.append(input("Input: "))
        except EOFError:
            break
    
    names = p.join(name_list)
    print(f"Adieu, adieu, to {names}")

main()