# Addition:
def add(n1,n2):
  return n1 + n2

# Subtraction:
def sub(n1,n2):
  return n1 - n2

# Multiplication:
def mul(n1,n2):
  return n1 * n2

# Division:
def div(n1,n2):
  return n1 / n2

# Dictionary:
operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}


def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
    operator = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    
    calculations_function = operations[operator]
    answer = calculations_function(num1,num2)
    print(f"{num1} {operator} {num2} = {answer}")
      
    if(input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ")=="y"):
      num1 = answer
    else:
      should_continue = False
      calculator()
  
calculator()