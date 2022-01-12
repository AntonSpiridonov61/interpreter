from enum import Enum, auto

class TokenType(Enum):
    INTEGER = auto()
    FLOAT = auto()
    EOS = auto()
    PLUS = auto()
    MINUS = auto()
    MUL = auto()
    DIV = auto()
    POW = auto()
    LPAREN = auto()
    RPAREN = auto()
    DOT = auto()
    SEMI = auto()
    ASSIGN = auto()
    VAR = auto()


class Token():
    def __init__(self, type_: TokenType, value: str) -> None:
        self.type_ = type_
        self.value = value

    def __str__(self) -> str:
        return f"Token({self.type_}, {self.value})"

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    print(list(TokenType))

    t = Token(TokenType.INTEGER, "2")
    print(t)