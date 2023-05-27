# Excepttional Handeling -------->
# try -->
# except --->
# else --->
# finally --->

# exception --> errors which come at runtime


while True:
    try:
        age=int(input("enter your age : "))
        break
    except ValueError:
        print('invalid input')

if age<18:
    print("You can't play this Game.")
else:
    print('You can play the Game.')
