print("hello") #hello

##
import random  # random - tool/module/library   - pre written code / functionality

cards = ["king", "queen", "Jack"]

choice = random.choice(cards)

print(choice) #randomly show one element


##
## Number guessing game
computer = random.randint(1, 5)

while True:
    guess = int(input("Try to guess the number: "))

    if guess == computer:
        print("You correctly guess the number")
        break

##
import datetime
from datetime import datetime, time, timedelta
today = datetime.today()
print(today) #2026-11-06 22:47:09.149516

x = today.strftime("Date: %Y-%m-%d  Time: %H:%M:%S  Day: %A")
print(x) #Date: 2026-11-06  Time: 22:49:26  Day: Friday





##
def divide(a, b):
  if b == 0:
    return "Cannot divide by zero"
  print("Hello World")
  return a/b
divide(10, 2) #Hello World, 5.0
divide(10, 0) #Cannot divide by zero