### input:
`BEGIN
    y := 2.7;
    BEGIN
        a := 3;
        a := a;
        b := 10 + a + 10 * y / 4;
        c := a - b
    END;
    x := 11;
END.`

### output:
`{'y': 2.7, 'a': 3, 'b': 19.75, 'c': -16.75, 'x': 11}`