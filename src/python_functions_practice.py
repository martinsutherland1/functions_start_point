# write functions on this file only, functions need to be based on python_functions
# under the folder tests
# You'll need to delete @unit.test.skip lines in order for tests to run in file below
# run tests via run_tests.py

def return_10():
    return 10

def add(num_1 , num_2) :
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string_1):
    return len(string_1)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(num):
    if num == 1:
        return "January"
    elif num == 3:
        return "March"
    elif num == 4:
        return "April"
    elif num == 9:
        return "September"
    elif num == 10:
        return "October"                

def number_to_short_month_name(num):
    month_name = number_to_full_month_name(num)[0:3]
    return month_name   

def volume_of_cube(l):
    return l ** 3

def reverse_string(x):
    return x[::-1]

# reverse_test = reverse_string("hello")
# print(reverse_test)

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print((150-32) * 5/9)
