import pytest
from interpreter.lexer import Lexer, LexerException
from interpreter.token import TokenType

@pytest.fixture
def testLexer() -> Lexer:
    return Lexer()

class TestLexer:

    def test_plus(self, testLexer: Lexer):
        testLexer.init('+')
        token = testLexer.next_()
        assert token.type_ == TokenType.PLUS

    def test_minus(self, testLexer: Lexer):
        testLexer.init('-')
        token = testLexer.next_()
        assert token.type_ == TokenType.MINUS

    def test_mul(self, testLexer: Lexer):
        testLexer.init('*')
        token = testLexer.next_()
        assert token.type_ == TokenType.MUL

    def test_div(self, testLexer: Lexer):
        testLexer.init('/')
        token = testLexer.next_()
        assert token.type_ == TokenType.DIV

    def test_pow(self, testLexer: Lexer):
        testLexer.init('^')
        token = testLexer.next_()
        assert token.type_ == TokenType.POW

    def test_lparen(self, testLexer: Lexer):
        testLexer.init('(')
        token = testLexer.next_()
        assert token.type_ == TokenType.LPAREN

    def test_rparen(self, testLexer: Lexer):
        testLexer.init(')')
        token = testLexer.next_()
        assert token.type_ == TokenType.RPAREN

    def test_integer(self, testLexer: Lexer):
        testLexer.init('10')
        token = testLexer.next_()
        assert token.type_ == TokenType.INTEGER and token.value == '10'

    def test_float(self, testLexer: Lexer):
        testLexer.init('5.2')
        token = testLexer.next_()
        assert token.type_ == TokenType.FLOAT and token.value == '5.2'

    def test_eos(self, testLexer: Lexer):
        testLexer.init(' \t\n')
        token = testLexer.next_()
        assert token.type_ == TokenType.EOS

    def test_dot(self, testLexer: Lexer):
        testLexer.init('.')
        token = testLexer.next_()
        assert token.type_ == TokenType.DOT

    def test_semi(self, testLexer: Lexer):
        testLexer.init(';')
        token = testLexer.next_()
        assert token.type_ == TokenType.SEMI

    def test_assignment(self, testLexer: Lexer):
        testLexer.init(':=')
        token = testLexer.next_()
        assert token.type_ == TokenType.ASSIGN

    def test_wrong_token(self, testLexer: Lexer):
        testLexer.init(':')
        with pytest.raises(LexerException):
            testLexer.next_()

    def test_wrong_number(self, testLexer: Lexer):
        testLexer.init('35.')
        with pytest.raises(LexerException):
            testLexer.next_()

    def test_var_name(self, testLexer: Lexer):
        testLexer.init('efe ')
        token = testLexer.next_()
        assert token.type_ == TokenType.VAR and token.value == 'efe'

    def test_scope_begin(self, testLexer: Lexer):
        testLexer.init('BEGIN ')
        token = testLexer.next_()
        assert token.type_ == TokenType.BEGIN and token.value == 'BEGIN'

    def test_scope_end(self, testLexer: Lexer):
        testLexer.init('END ')
        token = testLexer.next_()
        assert token.type_ == TokenType.END and token.value == 'END'