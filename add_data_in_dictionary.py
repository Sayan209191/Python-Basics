# add & delete data in dictionary ------->

user_info = {
    'name': 'sayan',
    'age': '18',
    'd_o_b': ['15-01-2004']
}

# how to add data ---->      syntax --> dictionaryname["key name"]=["value"]

user_info["fav_song"]=['song1','song2','song3']
print(user_info)

# pop method ----->

poped_item=user_info.pop('d_o_b')
print(user_info)
print(f"poped item is {poped_item}")


# popitem method -----> used randomly delete any key value pair --->

pope_item=user_info.popitem()
print(user_info)
print(f"randomly poped item is {pope_item}") 
