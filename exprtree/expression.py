"""expression that represents either a binary expression or unary expression
in a Abstract Syntax Tree (AST)
"""

class Expression:
    class OperatorError(Exception):
        def __init__(self, msg):
            print("Operator Error:", msg)

    ops = "*/+-~"

    @staticmethod
    def op_is_greater(op1, op2):
        if op1 == "~":
            return True
        elif op1 == "*" or op1 == "/":
            return op2 != "~"
        elif op1 == "+" or op1 == "-":
            return op2 not in "*/~"
        else:
            raise Expression.OperatorError("op1: {0}, op2: {1}".format(op1, op2))

class ConstantExpression(Expression):
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
        """Create a variable expression, where var is a string representing the variable"""
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
