       ##Parameter and Argument##

def greet (name): #here "name" is parameter
    print(f"Hello Mr. {name}")
    print(f"How's life going {name}?")

greet("Baten Mia") #here "Baten Mia" is Argument
#Hello Mr. Baten Mia
#How's life going Baten Mia?


## Default parameter
def greet (name="XYZ"): #here "XYZ" is default parameter
    print(f"Hello Mr. {name}")
    print(f"How's life going {name}?")

greet("HAS") #If write/input something(like HAS) then show this 
#Hello Mr. HAS
#How's life going HAS?

greet() #If empty then show default name
#Hello Mr. XYZ
#How's life going XYZ?