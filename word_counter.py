# define a function to count a chracter in  a string -----> store in a dictionary 

def word_counter(string):
    count={}
    for char in string:
        count[char]=string.count(char)
    return count

print(word_counter("sayan"))        