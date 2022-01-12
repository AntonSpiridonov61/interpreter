from interpreter import Parser, Interpreter

if __name__ == "__main__":
    parser = Parser()
    inter = Interpreter()

    print(inter.interpret(parser("3 * (5 + 3)")))
    print(inter.interpret(parser("1 * 7 + 3")))
    print(inter.interpret(parser("--1 + 3")))
    print(inter.interpret(parser("(1 + 1)^3^2")))
    print(inter.interpret(parser("7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)")))
    print(inter.interpret(parser("5 - - - + - (3 + 4) - +2")))