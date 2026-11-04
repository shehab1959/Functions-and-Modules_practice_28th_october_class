def coffee_machine(coffee,sugar,milk=10):
    print("Making: ", coffee,sugar,milk)
coffee_machine(20,5) #Making:  20 5 10
coffee_machine(20,5,30) #Making:  20 5 30


##
def coffee_machine(coffee,sugar,milk=10):
    print("Brewing....")
    cup = coffee + sugar + milk
    return cup

my_cup = coffee_machine(20,4)
print("Cup Size: ", my_cup, "g")

#Brewing....
#Cup Size:  34 g



##
def xyz(a,b):
    result = a + b
    return result
output1 = xyz(5,7)
print(output1) #12
output2 = xyz(output1,12)
print(output2) #24



##
def calculate_grade_print(marks):
    grade = "A" if marks >= 80 else "B" # logic
    print("Grade:", grade)
    return grade


# Output is shown, but cannot be reused
result = calculate_grade_print(85)
print("Stored result:", result)

if result == "A":
    print("Eligible for scholarship")
else:
    print("Keep improving!")

#Grade: A
#Stored result: A
#Eligible for scholarship