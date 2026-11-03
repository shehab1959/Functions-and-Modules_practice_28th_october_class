###Function basic Structure
def xyz(): #Function head
    print("Hello World") #Function body
xyz() #this is call "Function Call"


###Normally: (Example: 01)
price = 2000
tax_rate = 0.25
total_price = price + (price*tax_rate)
print("Total Price:",total_price) #Total Price: 2500.0

price = 2300
tax_rate = 0.25
total_price = price + (price*tax_rate)
print("Total Price:",total_price) #Total Price: 2875.0


##Now same thing using Function
def calculate_final_price(price):
    tax_rate = 0.25
    total_price = price + (price*tax_rate)
    print("Total Price:",total_price)

calculate_final_price(3000) #Total Price: 3750.0
calculate_final_price(3460) #Total Price: 4325.0
calculate_final_price(7460) #Total Price: 9325.0


###Normally: (Example: 02)
name = "Sadia"
print(f"Hello {name}")
print(f"How are you {name}")
#Hello Sadia
#How are you Sadia

name = "Shovon"
print(f"Hello {name}")
print(f"How are you {name}")
#Hello Shovon
#How are you Shovo





##Now same thing using Function
def greet(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")

greet("Shehab") 
#Hello Shehab
#How are you Shehab?
greet("Abdullah")
#Hello Abdullah
#How are you Abdullah?



##Using Function with list
def greet(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")
    
employee_list = ["Abir","Hasan","PK"]
for name in employee_list:
    greet(name)
#Hello Abir
#How are you Abir?
#Hello Hasan
#How are you Hasan?
#Hello PK
#How are you PK?