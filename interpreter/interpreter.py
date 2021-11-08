from interpreter.token import TokenType
from .node import Node, BinOp, UnOp, Number


class InterpreterException(Exception):
    pass

class Interpreter():

    def interpret(self, tree: Node) -> float:
        return self._visit(tree)

    def _visit(self, node: Node) -> float:
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, BinOp):
            return self._visit_binop(node)
        elif isinstance(node, UnOp):
            return self._visit_unop(node)

        raise InterpreterException("invalid node")


    def _visit_number(self, node: Number) -> float:
        return float(node.token)

    def _visit_binop(self, node: BinOp) -> float:
        op = node.op
        if op.type_ == TokenType.PLUS:
            return self._visit(node.left) + self._visit(node.right)
        if op.type_ == TokenType.MINUS:
            return self._visit(node.left) - self._visit(node.right)
        if op.type_ == TokenType.MUL:
            return self._visit(node.left) * self._visit(node.right)
        if op.type_ == TokenType.DIV:
            return self._visit(node.left) / self._visit(node.right)
        if op.type_ == TokenType.POW:
            return self._visit(node.left) ** self._visit(node.right)
        raise InterpreterException("invalid operator")

    def _visit_unop(self, node: UnOp) -> float:
        op = node.op
        if op.type_ == TokenType.PLUS:
            return self._visit(node.right)
        if op.type_ == TokenType.MINUS:
            return -self._visit(node.right)