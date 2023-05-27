# in keyword used to check the values & keys present or not ----->


user_info = {
    'name': 'sayan',
    'age': '18',
    'd_o_b': ['15-01-2004']
}

# for key --->

if 'name' in user_info:
    print("present")
else:
    print("not present")

# for values ------->

if 'sayan' in user_info.values():
    print("present")
else:
    print("not present ")

# for list ---->
if ['15-01-2004'] in user_info.values():
    print("present")
else:
    print("not present")
