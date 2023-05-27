# looping in list      ------>

user_info = {
    'name': 'sayan',
    'age': '18',
    'd_o_b': ['15-01-2004']
}

# for key --->

for i in user_info:
    print(i)

# values method in dictionary --->

user_info_values = user_info.values()
print(user_info_values)

# keys method ----->

user_info_keys = user_info.keys()
print(user_info_keys)

# for values ----->

for i in user_info.values():
    print(i)

# printing values by using keys ----->

for i in user_info:
    print(user_info[i])

# item method in loop ------>

user_info_items = user_info.items()
print(user_info_items)
print(type(user_info_items))

# item method in loop ---->

for key, values in user_info.items():
    print(f"the key is {key} and the value is {values}")
