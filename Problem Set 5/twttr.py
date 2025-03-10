#https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

def main():
    prompt = input("Input: ")
    res = shorten(prompt)
    print("Output:", res)


def shorten(prompt):
    formated = ""
    for i in prompt:
        if i not in "aeiouAEIOU":
            formated += i
    return formated

if __name__ == "__main__":
    main()