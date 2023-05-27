# read from a csv file and write in another csv file -------->

# import pdb
# pdb.set_trace()
from csv import DictReader,DictWriter
with open('final.csv','r') as rf:
    with open('file2.csv','w',newline='') as wf:
        csv_reader=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=['employee_name','lastname','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,lname,age=row['first_name'],row['last_name'],row['age']
            csv_writer.writerow({
                'emplyee_name':fname.upper(),
                'lastname':lname.upper(),
                'age':age,
            })
            
        
        