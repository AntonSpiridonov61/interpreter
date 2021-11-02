from .token import Token, TokenType
from .lexer import Lexer

class InterpreterException(Exception):
    pass

class Interpreter():

    def __init__(self):
        self._current_token: Token = None
        self._lexer = Lexer()

    def _check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next_()
        else:
            raise InterpreterException(f"Invalid token order {type_}")

    def _factor(self) -> float:
        token = self._current_token
        self._check_token_type(TokenType.INTEGER)
        return float(token.value)

    def _term(self) -> int:
        result = self._factor()
        ops = [TokenType.MUL, TokenType.DIV]
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.MUL:
                self._check_token_type(TokenType.MUL)
                result *= self._factor()
            elif token.type_ == TokenType.DIV:
                self._check_token_type(TokenType.DIV)
                result /= self._factor()
        
        return result

    def _expr(self) -> int:
        self._current_token = self._lexer.next_()
        ops = [TokenType.PLUS, TokenType.MINUS, TokenType.MUL, TokenType.DIV]
        result = self._term()
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.PLUS:
                self._check_token_type(TokenType.PLUS)
                result += self._term()
            elif token.type_ == TokenType.MINUS:
                self._check_token_type(TokenType.MINUS)
                result -= self._term()
            else:
                raise InterpreterException("Bad operator")

        return result

    def interpret(self, _text: str):
        self._lexer.init(_text)
        return self._expr()

    def __call__(self, _text: str) -> int:
        return self.interpret(_text)