from interpreter import Interpreter

if __name__ == "__main__":
    interpreter = Interpreter()
    print(interpreter("2+2"))
    print(interpreter("12-2"))
    print(interpreter.interpret("2+3"))