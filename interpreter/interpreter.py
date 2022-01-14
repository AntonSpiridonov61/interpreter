from interpreter.token import TokenType
from .node import Node, BinOp, UnOp, Number, Block, Assign, Var, NoOp


class InterpreterException(Exception):
    pass

class Interpreter():

    def __init__(self):
        self.GLOBAL_SCOPE = {}

    def interpret(self, tree: Node):
        return self._visit(tree)

    def _visit(self, node: Node) -> float:
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, BinOp):
            return self._visit_binop(node)
        elif isinstance(node, UnOp):
            return self._visit_unop(node)
        elif isinstance(node, Block):
            return self._visit_block(node)
        elif isinstance(node, Assign):
            return self._visit_assign(node)
        elif isinstance(node, Var):
            return self._visit_var(node)
        elif isinstance(node, NoOp):
            return self._visit_noop(node)

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

    def _visit_block(self, node: Block):
        for child in node.children:
            self._visit(child)

    def _visit_assign(self, node: Assign):
        var_name = node.left.value
        self.GLOBAL_SCOPE[var_name] = self._visit(node.right)

    def _visit_var(self, node: Var):
        var_name = node.value
        val = self.GLOBAL_SCOPE.get(var_name)
        if val is None:
            raise InterpreterException(f"invalid {node}")
        else:
            return val

    def _visit_noop(self, node: NoOp):
        pass