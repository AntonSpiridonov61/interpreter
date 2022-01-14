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
                return Token(TokenType.INTEGER, self._integer())

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

    def _integer(self):
        result: list = []
        while self._current_char and self._current_char.isdigit():
            result.append(self._current_char)
            self._forward()
        return "".join(result)

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
