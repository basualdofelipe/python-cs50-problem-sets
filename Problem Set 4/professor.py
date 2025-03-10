#https://cs50.harvard.edu/python/2022/psets/4/professor/

import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        score += problem(level)
    print("Score:", score)




def get_level():
    while True:
        level = get_int_input("Level: ")
        if level in [1, 2, 3]:
            return level
        else: pass



def generate_integer(level):
    range_start = 10**(level-1)
    range_end = (10**level)-1
    return random.randint(range_start, range_end)
    

def get_int_input(text):
    while True:
        try:
            number = int(input(text))
            break
        except ValueError:
            pass
    return number

def problem(level):
    x = generate_integer(level)
    y = generate_integer(level)
    res = x + y

    chance = 1

    while True:
        user_res = int(input(f"{x} + {y} = "))

        if user_res == res:
            return True
        else:
            if chance == 3:
                print("EEE")
                print(f"{x} + {y} = {res}")
                return False
            else:
                print("EEE")
                chance += 1



if __name__ == "__main__":
    main()