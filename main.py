from interpreter import Interpreter

if __name__ == "__main__":
    interpreter = Interpreter()
    print(interpreter("---2 + 2"))
    print(interpreter("((2 + 2) * 2) - (3 * 4)"))
    print(interpreter.interpret("7 / 2 * 3"))