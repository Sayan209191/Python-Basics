# it is use to check multiple statement checking ------>

age=int(input("enter your age :"))
if age==0 or age<0:
    print("You can't Watch the show.")
elif 0<age<=3:
    print("Ticket price : Free ")
elif 3<age<=10:
    print("Ticket price : 150 ")  
elif 10<age<60:
    print("Ticket price : 250 ") 
else:
    print("TIcket price : 200")  