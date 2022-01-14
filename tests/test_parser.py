import pytest
from interpreter.parser import Parser, ParserException
from interpreter.node import Node, BinOp, UnOp, Number, Block, Assign, Var, NoOp
from interpreter.token import Token, TokenType

@pytest.fixture
def testParser() -> Parser:
    return Parser()

@pytest.fixture
def empty():
    f = open('./textProgram/empty.txt')
    text = f.read()
    f.close()
    return text

@pytest.fixture
def program():
    with open('./textProgram/program2.txt') as f:
        return f.read()

@pytest.fixture
def wrongProgram():
    with open('./textProgram/wrong2.txt') as f:
        return f.read()



class TestParser:

    def test_empty(self, testParser, empty):
        assert isinstance(testParser.parse(empty), Node)

    def test_call(self, testParser, empty): 
        assert isinstance(testParser(empty), Node)

    def test_wrong_program_without_semi(self, testParser, wrongProgram):
        with pytest.raises(ParserException):
            testParser(wrongProgram)

    def test_wrong(self, testParser, program):
        program = program
        program = program.replace('BEGIN', 'END')
        with pytest.raises(ParserException):
            testParser(program)