def main():
    text = input("Expression: ")
    x, y, z = text.split(" ")
    res = math_interpreter(float(x), y, float(z))
    print(res)

def math_interpreter(x,y,z):

    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z

main()
"""

también así, pero más pegriloso
def otherone():
    text = input("Expression: ")
    print(eval(text))

otherone()
"""