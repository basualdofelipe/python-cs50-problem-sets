"""
Just setting up my twttr

When texting or tweeting, it's not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

def main():
    prompt = input("Input: ")
    res = twttr(prompt)
    print("Output:", res)


def twttr(prompt):
    formated = ""
    for i in prompt:
        if i not in "aeiouAEIOU":
            formated += i
    return formated

main()