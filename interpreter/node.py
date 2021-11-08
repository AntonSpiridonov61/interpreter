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