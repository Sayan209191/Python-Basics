# fromkeys method()----->

# used to create a dictionary ------> keys will be different but value will be same ------>

dictionary=dict.fromkeys(range(1,11),'unknown')     # using range function
print(dictionary)

string_dic=dict.fromkeys("abcd",'unknown')       # using string
print(string_dic)

list_dic=dict.fromkeys([1,2,3,4,5,6,7],'unknown')
print(list_dic)