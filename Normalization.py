age = 80
max_age = 120
print(age/max_age) #0.666666666666

#
salary = 60000
max_salary = 350000
print(salary/ max_salary) #0.17142857142857143

#
def normalize_data(value, max_value):
    # Normalize value between 0 and 1
    normalized = value / max_value
    print(f"Original value: {value} | Normalized value: {normalized}")

# Passing arguments into the function
normalize_data(80, 120) #Original value: 80 | Normalized value: 0.6666666666666666
normalize_data(60000, 350000) #Original value: 60000 | Normalized value: 0.17142857142857143
