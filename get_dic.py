# get method ------->
# used to find the the item ---->

user_info = {
    'name': 'sayan',
    'age': '18',
    'd_o_b': ['15-01-2004'],
    'hobby':'coading , cricket',
    'fav_song':['song1','song2','song3']
    ,
}

print(user_info['name'])     # in this way we can earn value of the key 

print(user_info.get('name'))    # this is better than it 

# supppose any key does't exit in dictionry -----> 
# 1 . process show error 
# 2. get method show "None"     so get method is better

print(user_info.get('names'))

# supppose any key does't exit in dictionry  ---> 

#  if we don't return "None" and return  any argument then we do ------->

# syntax ----> dic_name.get('key','argument')

print(user_info.get('fav','not found !!!'))

