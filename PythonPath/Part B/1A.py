ser_input_list=[int(input('Enter the {} element'.format(i+1))) for i in range(5)]

unique_elements=set(user_input_list)

print('user input',user_input_list)
print('unique elemetns',unique_elements)

odd_numbers_list=[i for i in range(10) if i%2==0]
reversed_odd_numbers_list=reversed(odd_numbers_list)

print(odd_numbers_list)
print(list(reversed_odd_numbers_list))