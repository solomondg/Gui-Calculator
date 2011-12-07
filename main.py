import math
import random

num1 = 0
num2 = 0
op = 0
answer = 0

class input:
  """handles inputes."""
  def __init__(self):
    num1 = 0
    num2 = 0
    op = ''
    num1 = exec(input("enter a number: "))
    num2 = exec(input("enter another number: "))
    op = exec(input("enter an operator"))

class eval:
  """evaluates the numbers"""
  def __init__(self):
    self.bad_op_responce = 0
    if op == '+':
      answer = num1 + num2
    elif op == '-':
      answer = num1 - num2
    elif op == '*' || 'x' || 'X':
      answer = num1 * num2
    elif op == '/' || '÷':
      answer = num1 / num2
    elif op == '%':
      answer = num1 % num2
    else:
      bad_op_responce = random.randint(1, 5)
      if bad_op_responce == 1:
        print "Please input a number taught in elementry school."
      if bad_op_responce == 2:
        print "error.... error.... operator not found in memory banks. shutting down.......... \n \n *bzzzt*"
      if bad_op_responce == 3:
        print "Really? this is a CALCULATOR, not a AI! How is it expected to know every single operator in THE WHOLE FLIPPING WORLD?"
      if bad_op_responce == 4:
        print "That operator is only known to the Aztecs. Please consult them for the correct answer"
      if bad_op_responce == 5:
        print "Please do not use whatever strange alien operator you are using, and only use +, -, *, /, and %"