# # Array Review
#
# practice_array = ['kevin', 'bob', 'kenn', 'john', 'bill', 'kevin']



# # where_el_at = practice_array.index('bill')
# # print(where_el_at)
# # print(practice_array[where_el_at])
#
# num_array = [34, 765, 54, 88, 546, 321]
# print(num_array)
#
# print(sum(num_array))
# print(max(num_array))
# print(min(num_array))
# print(practice_array.count('kevin'))
#
#
#
#
# # Get element
# my_el = practice_array[2]
# print(my_el)
#
# # add element
# practice_array.append('chuck')
# print(practice_array)
#
# delete
#
# del
# del practice_array[2]
# print(practice_array)
#
# popped_el = practice_array.pop(4)
# practice_array.pop(4)
#
# retel = practice_array.remove('kevin')
#
# print(practice_array)
# print(retel)
#
# print(popped_el)
#
# Problem 4:
# Use the following list of 5 numbers. score_list = [21,14,6,8,28,42,21]

# Write the code to find the element where the score is equal to 6
score_list = [21, 14, 777, 228, 2328, 2224, 6, 2, 21]

idx_6 = score_list.index(6)
print(f'The value at index position {idx_6} and the value is {score_list[idx_6]}')

