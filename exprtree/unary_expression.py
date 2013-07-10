"""an unary expression that stores an operator and an operand"""
from expression import Expression, ConstantExpression
import operator

class UnaryExpression(Expression):
    def evaluate(self, variables):
        return self.operator(self.operand.evaluate(variables))

    def cfold(self):
        self.operator = self.operator
        self.operand = self.operand.cfold()

        if isinstance(self.operand, ConstantExpression):
            return ConstantExpression(self.evaluate({}))
        else:
            return self

    def __str__(self):
        return "(" + self._op_sym + str(self.operand) + ")"

    def __repr__(self):
        return self.__str__();

class NegateExpression(UnaryExpression):
    def __init__(self, operand):
        self.operator = operator.neg
        self.operand = operand
        self._op_sym = "~"
