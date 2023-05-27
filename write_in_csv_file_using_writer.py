from csv import writer
with open('file.csv','a',newline='') as f:
    csv_writer=writer(f)
    
    # 2 methods ---> 1. writerow , 2. writerows
    
    # writerow method ---------->
    
    csv_writer.writerow(['Name','Country'])
    csv_writer.writerow(['Sayan','INDIA'])
    csv_writer.writerow(['Soumya','INDIA'])
    
    # writerows method --------->
    
    csv_writer.writerows([['Namita','India']])