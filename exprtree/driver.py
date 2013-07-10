"""Handles the execution of expression trees """
from expression import *
from binary_expression import *
from unary_expression import *

# Invariant:
# 	op_stack has string items in "*/+=~()"
output_q = list()
op_stack = list()

def create_expr(operator, operand1, operand2=None):
    """Given an operator symbol and operand/s, construct the appropriate expression
    according to the symbol.

    """

    if operator == "*":
        return TimesExpression(operand1, operand2)
    elif operator == "/":
        return DivideExpression(operand1, operand2)
    elif operator == "+":
        return PlusExpression(operand1, operand2)
    elif operator == "-":
        return SubtractExpression(operand1, operand2)
    elif operator == "~":
        return NegateExpression(operand1)
    else:
        raise Expression.OperatorError

def build_ast():
    """Using the output_q, create the AST that represents the parsed expression
    """

    # list of temporary operands: invariant is that this list contains all
    # expression types
    operands = list()

    # loop through the output queue and construct the ast by creating expressions
    # if the operator and the necessary operands are given
    while(len(output_q) > 0):
        item = output_q.pop()

        if isinstance(item, int):
            operands.append(ConstantExpression(item))
        elif item in Expression.ops:
            if item == "~":
                operands.append(create_expr(item, operands.pop()))
            else:
                operand2 = operands.pop()
                operand1 = operands.pop()
                operands.append(create_expr(item, operand1, operand2))
        else:
            operands.append(VariableExpression(item))

    print(operands)

    assert(len(output_q) == 0)
    assert(len(operands) == 1)

    return operands.pop()

def parse(expr_str):
    """Given an expression string, parse it into an appropriate expression.

    For example:
    : (~x) => UnaryExpression of negative operator and VariableExpression of x
    : (x+3) => BinaryExpression of plus operator and VariableExpression of x and
    ConstantExpression of 3

    Employs the Shuning-yard algorithm in parsing the string into an AST:
    http://en.wikipedia.org/wiki/Shunting-yard_algorithm

    """

    # since the string is parsed one character a time, must
    # accumulate number for multi-digit numbers
    num_acc = 0
    record_num = False

    del output_q[:]
    del op_stack[:]

    for c in expr_str.replace(" ", ""):
        # Loop through the expression string one character at a time and create
        # a RPN (reverse polish notation) of the expression

        if c.isnumeric():
            num_acc = num_acc * 10 + int(c)
            record_num = True

        else:
            if num_acc:
                # end of number accumulation for this specific number
                output_q.insert(0, num_acc)
                num_acc = 0
                record_num = False

            if c.isalpha():
                # any one character is a variable
                output_q.insert(0, c)

            elif c == "(":
                op_stack.append("(")

            elif c == ")":
                # pop stack until either "(" or throw error
                item = op_stack.pop()
                while item != "(":
                    output_q.insert(0, item)
                    item = op_stack.pop()

            else:
                # handle operators
                if op_stack:
                    op2 = op_stack.pop()
                    if op2 in Expression.ops and Expression.op_is_greater(op2, c):
                        output_q.insert(0, op2)
                    else:
                        op_stack.append(op2)
                op_stack.append(c)

    # Handle leftovers
    if record_num:
        output_q.insert(0, num_acc)

    # Pop remaining operators from the operator stack
    while len(op_stack) > 0:
        item = op_stack.pop()
        output_q.insert(0, item)

    assert(len(op_stack) == 0)

    print("Op Stack", op_stack)
    print("Output Q", output_q)

def run():
    expression = input("eval: ")
    parse(expression)
    build_ast()

if __name__ == "__main__":
    run()
