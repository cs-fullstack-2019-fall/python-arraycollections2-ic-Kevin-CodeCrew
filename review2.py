Client needs a function that can be used for temperature conversion (C/F)

The function should take a temp, and a scale (C or F) parameter

Print the proper conversion for data/option passed in

=======================================================
Conversion formulas:

celsius_temp_val = (fahrenheit_temp_val - 32) * 5.0 / 9.0

fahrenheit_temp_val = 9.0 / 5.0 * celsius_temp_val + 32



# # Convert Celsius to Fahrenheit
#
# def convert_temerature(temp_value, conversion_flag):
#     c_result = -1
#
#     if conversion_flag == 'C':
#         c_result = (temp_value - 32) * 5.0 / 9.0
#     else:
#         c_result = 9.0 / 5.0 * temp_value + 32
#
#     return c_result
#
#
# # print(convert_temerature(212,'C'))
#
#
# user_choice = input("Enter F to convert to Fahrenheit or C for Celcius: ")
# user_temp = int(input("Enter teperature:"))
#
# conversion_result = convert_temerature(user_temp, user_choice)
#
# print("Temperature:", user_temp, "Converted = ", conversion_result, " F")

# Lists/arrays

name_list = ['kevin', 'george', 'nick', 'sam']
# print(name_list[1:3])
# print(name_list[2:])
# print(name_list[:1])

def main_pgm():
    ff_result = firstFunction()
    print(ff_result)













