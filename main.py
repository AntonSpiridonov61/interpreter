from interpreter import Parser, Interpreter

if __name__ == "__main__":
    interpret = Interpreter()
    text = """
        BEGIN
            y := 2.7;
            BEGIN
                a := 3;
                a := a;
                b := 10 + a + 10 * y / 4;
                c := a - b
            END;
            x := 11;
        END.
    """
    f = open('./textProgram/wrong2.txt')
    text = f.read()
    f.close()
    print(interpret(text))
