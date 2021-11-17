import calendar

def return_10():

    return 10

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2


def divide(num1,num2):
    return num1 / num2

def length_of_string(str1):
    return len(str1)

def join_string( string_1, string_2 ):
    return string_1 + string_2

def add_string_as_number(str_1, str_2):
    return int(str_1) +int(str_2)

def number_to_full_month_name(num):
    return calendar.month_name[num]

def number_to_short_month_name(num):
    return calendar.month_abbr[num]
def volume_of_cube(side):
    return side*side*side

def reverse_string(str):
    return str[::-1]


    
