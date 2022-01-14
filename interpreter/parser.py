from .token import Token, TokenType
from .lexer import Lexer
from .node import Node, BinOp, UnOp, Number, Block, Assign, Var, NoOp


class ParserException(Exception):
    pass

class Parser():

    def __init__(self):
        self._current_token: Token = None
        self._lexer = Lexer()

    def _check_token_type(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next_()
        else:
            raise ParserException(f"Invalid token order {type_}, {self._current_token}")

    def _program(self) -> Node:
        node = self._complex_statement()
        self._check_token_type(TokenType.DOT)
        return node

    def _complex_statement(self):
        self._check_token_type(TokenType.BEGIN)
        nodes = self._statement_list()
        self._check_token_type(TokenType.END)

        root = Block()
        for node in nodes:
            root.children.append(node)

        return root

    def _statement_list(self):
        node = self._statement()
        results = [node]

        while self._current_token.type_ == TokenType.SEMI:
            self._check_token_type(TokenType.SEMI)
            results.append(self._statement())

        if self._current_token.type_ == TokenType.VAR:
            raise ParserException(f"Invalid type {self._current_token.type_}")

        return results

    def _statement(self) -> Node:
        if self._current_token.type_ == TokenType.BEGIN:
            node = self._complex_statement()
        elif self._current_token.type_ == TokenType.VAR:
            node = self._assignment_statement()
        else:
            node = self._empty()
        return node

    def _assignment_statement(self) -> Node:
        left = self._variable()
        token = self._current_token
        self._check_token_type(TokenType.ASSIGN)
        right = self._expr()
        return Assign(left, token, right)

    def _variable(self) -> Node:
        node = Var(self._current_token)
        self._check_token_type(TokenType.VAR)
        return node

    def _empty(self) -> Node:
        return NoOp()

    def _factor(self) -> Node:
        token = self._current_token

        if token.type_ == TokenType.PLUS:
            self._check_token_type(TokenType.PLUS)
            return UnOp(token, self._factor())
        elif token.type_ == TokenType.MINUS:
            self._check_token_type(TokenType.MINUS)
            return UnOp(token, self._factor())
        elif token.type_ == TokenType.INTEGER:
            self._check_token_type(TokenType.INTEGER)
            return Number(token)
        elif token.type_ == TokenType.FLOAT:
            self._check_token_type(TokenType.FLOAT)
            return Number(token)
        elif token.type_ == TokenType.LPAREN:
            self._check_token_type(TokenType.LPAREN)
            result = self._expr()
            self._check_token_type(TokenType.RPAREN)
            return result
        elif token.type_ == TokenType.VAR:
            return self._variable()
        else:
            raise ParserException(f"Invalid factor {token}")

    def _pow(self) -> Node:
        result = self._factor()
        ops = [TokenType.POW]
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.POW:
                self._check_token_type(TokenType.POW)
            result = BinOp(result, token, self._factor())
        return result   

    def _term(self) -> Node:
        result = self._pow()
        ops = [TokenType.MUL, TokenType.DIV]

        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.MUL:
                self._check_token_type(TokenType.MUL)
            else:
                self._check_token_type(TokenType.DIV)
            result = BinOp(result, token, self._pow())
        return result

    def _expr(self) -> Node:
        ops = [TokenType.PLUS, TokenType.MINUS]
        result = self._term()
        while self._current_token.type_ in ops:
            token = self._current_token
            if token.type_ == TokenType.PLUS:
                self._check_token_type(TokenType.PLUS)
            else:
                self._check_token_type(TokenType.MINUS)
            result = BinOp(result, token, self._term())

        return result

    def parse(self, text: str) -> Node:
        self._lexer.init(text)
        self._current_token = self._lexer.next_()
        return self._program()

    def __call__(self, text: str):
        return self.parse(text)