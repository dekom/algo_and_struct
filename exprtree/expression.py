"""expression that represents either a binary expression or unary expression
in a Abstract Syntax Tree (AST)
"""

class Expression:
    class OperatorError(Exception):
        def __init__(self, msg):
            print("Operator Error:", msg)

    op_precedence = {
        "~" : 5,
        "*" : 4,
        "/" : 4,
        "+" : 3,
        "-" : 3
    }

    ops = op_precedence.keys()

    @staticmethod
    def op_is_greater(op1, op2):
        return Expression.op_precedence[op1] >= Expression.op_precedence[op2]

class ConstantExpression(Expression):
    """An expression representing a numerical constant"""
    def __init__(self, value):
        assert(isinstance(value, int))
        self.value = value

    def evaluate(self, variables={}):
        return self.value

    def cfold(self):
        return self;

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

class VariableExpression(Expression):
    """Represents a variable such as 'x' and 'y' in 'x+y'"""
    def __init__(self, var):
        assert(isinstance(var, str))
        self.var = var

    def evaluate(self, variables):
        return variables[self.var]

    def cfold(self):
        return self

    def __str__(self):
        return str(self.var)

    def __repr__(self):
        return self.__str__()
