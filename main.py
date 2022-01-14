from interpreter import Parser, Interpreter

if __name__ == "__main__":
    parser = Parser()
    inter = Interpreter()

    text1 = """
        BEGIN
        END.
    """

    text2 = """
        BEGIN
	        x:= 2 + 3 * (2 + 3);
            y:= 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1));
        END.
    """

    text3 = """
        BEGIN
            y := 2;
            BEGIN
                a := 3;
                a := a;
                b := 10 + a + 10 * y / 4;
                c := a - b
            END;
            x := 11;
        END.
    """
    
    inter.interpret(parser(text1))
    print(inter.GLOBAL_SCOPE)