# update method in dictionary ---->

user_info = {
    'name': 'sayan',
    'age': '18',
    'd_o_b': ['15-01-2004']
    ,
}

more_info={
    'hobby':'coading , cricket',
    'fav_song':['song1','song2','song3']
    ,
}

user_info.update(more_info)
print(user_info)

# if we pass empty dictionary then nothing add or substract ---->
# if we pass any same key but different value ---> then updae method update the latest value 


more_info1={
    'name': 'Sayan Ghorui'
    ,
}
user_info.update(more_info1)
print(user_info)