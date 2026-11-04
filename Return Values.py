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