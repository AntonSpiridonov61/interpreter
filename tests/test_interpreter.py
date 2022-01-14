import pytest
from interpreter.interpreter import Interpreter, InterpreterException

@pytest.fixture
def testInterpreter():
    return Interpreter()

@pytest.fixture
def empty():
    with open('./textProgram/empty.txt') as f:
        return f.read()

@pytest.fixture
def program1():
    with open('./textProgram/program1.txt') as f:
        return f.read()

@pytest.fixture
def program2() -> str:
    with open('./textProgram/program2.txt') as f:
        return f.read()

@pytest.fixture
def program3() -> str:
    with open('./textProgram/program3.txt') as f:
        return f.read()

@pytest.fixture
def wrongProgram() -> str:
    with open('./textProgram/wrong.txt') as f:
        return f.read()

# @pytest.mark.parametrize(
#     "program, result",
#     [(program1(), {}), 
#     (program2(), {'a': 3, 'x': 2.0}), 
#     (program3(), {'x': -3.0, 'y': 2 })]
# )

class TestInterpreter:

    def test_none(self, testInterpreter):
        assert testInterpreter(None) == {}

    def test_empty(self, testInterpreter, empty):
        assert testInterpreter(empty) == {}

    def test_program1(self, testInterpreter, program1):
        assert testInterpreter(program1) == {'a': 17, 'b': 11.0}

    def test_program2(self, testInterpreter, program2):
        assert testInterpreter(program2) == {'a': -5.0, 'b': 6.9}

    def test_program3(self, testInterpreter, program3):
        assert testInterpreter(program3) == {'a': 10, 'b': 4.2, 'c': 14.2}

    def test_wrong_program(self, testInterpreter, wrongProgram):
        with pytest.raises(InterpreterException):
            testInterpreter(wrongProgram)