import math

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
    if op == '