import math
import random

class Main:
  """handles inputes and evaluates the problem."""
  def __init__(self):
    self.num1 = exec(input("enter a number: "))
    self.num2 = exec(input("enter another number: "))
    self.op = exec(input("enter an operator"))
    if self.op == '+':
      self.answer = self.num1 + self.num2
    elif self.op == '-':
      self.answer = self.num1 - self.num2
    elif self.op == '*' || 'x' || 'X':
      self.answer = self.num1 * self.num2
    elif self.op == '/' || '÷':
      self.answer = self.num1 / self.num2
    elif self.op == '%':
      self.answer = self.num1 % self.num2
    else:
      self.bad_op_responce = random.randint(1, 5)
      if self.bad_op_responce == 1:
        print "Please input a number taught in elementry school."
      if self.bad_op_responce == 2:
        print "error.... error.... operator not found in memory banks. shutting down.......... \n \n *bzzzt*"
      if self.bad_op_responce == 3:
        print "Really? this is a CALCULATOR, not a AI! How is it expected to know every single operator in THE WHOLE FLIPPING WORLD?"
      if self.bad_op_responce == 4:
        print "That operator is only known to the Aztecs. Please consult them for the correct answer"
      if self.bad_op_responce == 5:
        print "Please do not use whatever strange alien operator you are using, and only use +, -, *, /, and %"
      print str(self.answer)