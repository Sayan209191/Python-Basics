# what is dictionray ?
# ---> unordererd collection of data in key : value pair.

# why we are using dictionaries ?
# --> because of limitation of list does't represent real life data


# how to create a dictionary ?

user = {'name': 'sayan', 'age': '18', 'd_o_b': ['15-01-2004']}
print(user)
print(type(user))


# another style --->
user_info = {
    'name': 'sayan',
    'age': '18',
    'd_o_b': ['15-01-2004']
}
print(user_info)


# second method ---->

user1 = dict(name='sayan', age='18')
print(user1)
print(type(user1))

# how to accress data from dictionary ------->

print(user['name'])
# print(user_info['age'])

# dictionary in dictionary    ----->

users = {
    'user_1': {
        'name': 'sayan',
        'age': 18,
        'd_o_b': ['15-01-2004']
    },
    'user_2': {
        'name': 'sayan',
        'age': '18',
        'd_o_b': ['15-01-2004']
    }
}
# print(users)

# how to add data in empty dictionary or a dictionary   ------>

number = {}
number['num1'] = '10'
print(number)
number['num2'] = '20'
number['num3'] = '30'
number['num4'] = '50'
print(number)
