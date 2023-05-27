from csv import DictWriter
with open('final.csv','a',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['first_name','last_name','age'])
    csv_writer.writeheader()
    
    # Writerow and Writerows are two method 
    
    # 1. Writerow ------->
     
    csv_writer.writerow({
        'first_name':'Sayan',
        'last_name':'Ghorui',
        'age':19
    })
    csv_writer.writerow({
        'first_name':'Soumya',
        'last_name':'Ghorui',
        'age':15
    })
    csv_writer.writerow({
        'first_name':'Parimal',
        'last_name':'Ghorui',
        'age':45
    })
    csv_writer.writerow({
        'first_name':'Namita',
        'last_name':'Ghorui',
        'age':39
    })
    csv_writer.writerow({
        'first_name':'Ponchubala',
        'last_name':'Ghorui',
        'age':65
    })
    
    # 2. writerows ---->
    
    csv_writer.writerows([
        {'first_name':'Nirmal','last_name':'Ghorui','age':50}
    ])