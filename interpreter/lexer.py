from .token import Token, TokenType

class LexerException(Exception):
    pass

class Lexer():

    def __init__(self):
        self._pos: int = 0
        self._current_char: str = ''
        self._text: str = ''
        self.RESERVED_WORDS = {
            'BEGIN': Token(TokenType.BEGIN, 'BEGIN'),
            'END': Token(TokenType.END, 'END'),
        }

    def next_(self) -> Token:
        while self._current_char != None:
            if self._current_char.isspace():
                self._skip()
                continue
            if self._current_char.isdigit():
                return self._digit()

            char = self._current_char
            
            if self._current_char == "+":
                self._forward()
                return Token(TokenType.PLUS, char)
            if self._current_char == "-":
                self._forward()
                return Token(TokenType.MINUS, char)
            if self._current_char == "*":
                self._forward()
                return Token(TokenType.MUL, char)
            if self._current_char == "/":
                self._forward()
                return Token(TokenType.DIV, char)
            if self._current_char == "^":
                self._forward()
                return Token(TokenType.POW, char)
            if self._current_char == "(":
                self._forward()
                return Token(TokenType.LPAREN, char)
            if self._current_char == ")":
                self._forward()
                return Token(TokenType.RPAREN, char)
            if self._current_char == ".": 
                self._forward()
                return Token(TokenType.DOT, char)
            if self._current_char == ";":
                self._forward()
                return Token(TokenType.SEMI, char)
            if self._current_char == ':' and self._peek() == '=':
                self._forward()
                self._forward()
                return Token(TokenType.ASSIGN, ':=')
            if self._current_char.isalpha():
                return self._var()

            raise LexerException(f"Bad token {self._current_char}")
        return Token(TokenType.EOS, None)

    def _skip(self):
        while self._current_char and self._current_char.isspace():
            self._forward()

    def _digit(self):
        result: list = []
        while self._current_char and self._current_char.isdigit():
            result.append(self._current_char)
            self._forward()
        if self._current_char == ".": 
            result.append(self._current_char)
            self._forward()
            while self._current_char and self._current_char.isdigit():
                result.append(self._current_char)
                self._forward()
            if result[-1] == ".": 
                raise LexerException("invalid number")
            return Token(TokenType.FLOAT, "".join(result))
        return Token(TokenType.INTEGER, "".join(result))

    def _forward(self):
        self._pos += 1
        if self._pos >= len(self._text):
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def _peek(self):
        peek_pos = self._pos + 1
        if peek_pos > len(self._text) - 1:
            return None
        else:
            return self._text[peek_pos]

    def _var(self):
        res = ''
        while self._current_char and self._current_char.isalpha():
            res += self._current_char
            self._forward()
        token = self.RESERVED_WORDS.get(res, Token(TokenType.VAR, res))
        return token

    def init(self, _text: str) -> int:
        self._text = _text
        self._pos = -1
        self._forward()

# if __name__ == "__main__":
#     text3 = """
#         BEGIN
#             y := 2.5;
#             BEGIN
#                 a := 3;
#                 a := a;
#                 b := 10 + a + 10 * y / 4;
#                 c := a - b
#             END;
#             x := 11;
#         END.
#     """

#     lexer = Lexer()
#     lexer.init(text3)

#     for i in range(50):
#         print(lexer.next_())

