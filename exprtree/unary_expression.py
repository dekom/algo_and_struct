"""an unary expression that stores an operator and an operand"""
from expression import Expression, ConstantExpression
import operator

class UnaryExpression(Expression):
    def __init__(self, sym, operator, operand):
        """construct an unary expression when given an operator, which is a
        function, and operand is an expression that when evaluated, should
        return a value that the operator can expect"""
        self.operator = operator
        self.operand = operand
        self.__op_sym = sym

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
        return "(" + self.__op_sym + str(self.operand) + ")"

    def __repr__(self):
        return self.__str__();

class NegateExpression(UnaryExpression):
    def __init__(self, operand):
        super().__init__("~", operator.neg, operand)
