"""the set of binary expressions that have an operator and two operands"""
from expression import Expression, ConstantExpression
import operator

class BinaryExpression(Expression):
    def evaluate(self, variables={}):
        return self.operator(self.left.evaluate(variables),
                             self.right.evaluate(variables))

    def __str__(self):
        return "(" + str(self.left) + self._op_sym + \
            str(self.right) + ")"

    def __repr__(self):
        return self.__str__()

    def cfold(self):
        left = self.left.cfold()
        right = self.right.cfold()

        if isinstance(left, ConstantExpression) and \
           isinstance(right, ConstantExpression):
            return ConstantExpression(self.evaluate())
        else:
            return BinaryExpression(self.operator, left, right, self._op_sym)

class PlusExpression(BinaryExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self._op_sym = '+'
        self.operator = operator.add

class SubtractExpression(BinaryExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self._op_sym = '-'
        self.operator = operator.sub

class TimesExpression(BinaryExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self._op_sym = '*'
        self.operator = operator.mul

class DivideExpression(BinaryExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self._op_sym = '/'
        self.operator = operator.truediv
