"""the set of binary expressions that have an operator and two operands"""
from expression import Expression, ConstantExpression
import operator

class BinaryExpression(Expression):

    def __init__(self, operator, left, right, sym):
        """construct an binary expression when given an operator, which is a
        function, and the left and right expressions that, when evaluated,
        would return values that the operator accepts"""
        self.operator = operator
        self.left = left
        self.right = right
        self.__op_sym = sym

    def evaluate(self, variables={}):
        return self.operator(self.left.evaluate(variables),
                             self.right.evaluate(variables))

    def __str__(self):
        return "(" + str(self.left) + self.__op_sym + \
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
            return BinaryExpression(self.operator, left, right, self.__op_sym)

class PlusExpression(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(operator.add, left, right, '+')
        self.__op_sym = '+'

class SubtractExpression(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(operator.sub, left, right, '-')
        self.__op_sym = '-'

class TimesExpression(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(operator.mul, left, right, '*')
        self.__op_sym = '*'

class DivideExpression(BinaryExpression):
    def __init__(self, left, right):
        super().__init__(operator.truediv, left, right, '/')
        self.__op_sym = '/'
