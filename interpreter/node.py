from .token import Token


class Node():

    def __str__(self):
        return f"{self.__class__.__name__}"

class Number(Node):

    def __init__(self, token: Token) -> None:
        super().__init__()
        self.token = token

    def __str__(self) -> str:
        return f"Number({self.token}, {self.token})"


class BinOp(Node):

    def __init__(self, left: Node, op: Token, right: Node) -> None:
        self.left = left
        self.op = op
        self.right = right

    def __str__(self) -> str:
        return f"BinOp{self.op.value}({self.left}, {self.right})"


class UnOp(Node):

    def __init__(self, op: Token, right: Node) -> None:
        self.op = op
        self.right = right

    def __str__(self) -> str:
        return f"UnOp({self.op.value}{self.right})"


class Block(Node):

    def __init__(self):
        self.children = []

    def __str__(self) -> str:
        return f"Block({self.children})"


class Assign(Node):

    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __str__(self) -> str:
        return f"Assign{self.token}({self.left}, {self.right})"

class Var(Node):
    
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __str__(self) -> str:
        return f"Var({self.token}, {self.value})"

class NoOp(Node):
    pass