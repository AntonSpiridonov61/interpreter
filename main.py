from interpreter import Parser, Interpreter

if __name__ == "__main__":
    parser = Parser()
    inter = Interpreter()

    print(inter.interpret(parser("3 * (5 + 3)")))
    print(inter.interpret(parser("1 * 7 + 3")))
    print(inter.interpret(parser("--1 + 3")))
    print(inter.interpret(parser("(1 + 1)^3^2")))
