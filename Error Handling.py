def divide(a, b):
  return a/b

#print(divide(10, 0)) #error (ZeroDivisionError)


##
def divide(a, b):
    if b == 0:
      return "Division not possible"
    return a/b
print(divide(10, 3)) #3.3333333333333335
print(divide(10, 0)) #Division not possible
#print(divide(10, "a")) #error (TypeError)


##
def safe_divide(a, b):
    try:
        if b==0 :
            return "Not possible"
        result = a / b
        return result
    except Exception as e:  # Except - All error
        return e

print(safe_divide(10, 2)) #5.0
print(safe_divide(10, 0)) #Not possible
print(safe_divide(10, "a")) #error (unsupported operand type(s) for /: 'int' and 'str')



##
def safe_divide(a, b):
    try:
        result = a / b
        return result
    # custom user friendly messages for each errors (2 except blocks)
    except ZeroDivisionError:
        return "Error: You cannot divide by zero!"
    except TypeError:
        return "Error: Please provide numeric values only."

print(safe_divide(10, 2)) #5.0
print(safe_divide(10, 0)) #Error: You cannot divide by zero!
print(safe_divide(10, "a")) #Error: Please provide numeric values only.



##
def safe_divide(a, b):
    try:
        return a / b
    # a single custom error message for all errors
    except Exception:
        return "Error: Something went wrong. Please check your input."

print(safe_divide(10, 2)) #5.0
print(safe_divide(10, 0)) #Error: Something went wrong. Please check your input.
print(safe_divide(10, "a")) #Error: Something went wrong. Please check your input.