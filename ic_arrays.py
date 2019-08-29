# # In class array practice

# person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
# print(person_array[1])
# print(person_array[0], person_array[3])
# print(person_array[0], person_array[-1])
# print(person_array[0], person_array[len(person_array) - 1])
# # take out seconf el
# person_array.pop(1)
# print(person_array)

# Problem 2:
#
# Ask the User for a starting and ending number
# Write a function that takes the 2 numbers as parameters and builds a list/array of numbers with the values from start to end parameters and return the array to the caller
# Print the sum of the numbers in the list using an 'f' string (ex. The sum of the numbers from 5 to 100 is5050```)

def twoNum(num, num2):
    # emptyArray = []
    # for x in range(num, num2 + 1):
    #     emptyArray.append(x)

    newArray = list(range(num, num2))
    return newArray


num1 = int(input('enter start'))
num2 = int(input('enter end'))
new_array = twoNum(num1, num2)


print(f"The array of the two numbers are {new_array}")
