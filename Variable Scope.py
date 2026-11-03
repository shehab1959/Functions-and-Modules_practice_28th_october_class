##Local scope
def greet():
    user = "Sayem"   # local scope
    print(f"Hello, welcome back {user}")
greet() #Hello, welcome back Sayem
#print(user) #error because cannot access from inside of function, by outside function call.


##Global scope
user_name = "Jahid"  # global scope

def greet_v2():
    print(f"Hello, welcome back {user_name}")

greet_v2() #Hello, welcome back Jahid
print(user_name) #Jahid, here variable `user_name` can be accessed outside of the function


###
def simple_calculator(a,b):
    print(f"Addition: {a+b}")
    print(f"Subtraction: {a-b}")
    print(f"Multiplication: {a*b}")
    print(f"Division: {a/b}")
    return

result = simple_calculator(10, 5)
print(result) 
#Addition: 15
#Subtraction: 5
#Multiplication: 50
#Division: 2.0


##
add_result, sub_result, mul_result, div_result = simple_calculator(20, 5) 

print(add_result) #25
print(sub_result) #15
print(mul_result) #100
print(div_result) #4