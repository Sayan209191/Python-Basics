from csv import reader
with open('file1.csv','r') as f:
    csv_reader=reader(f)   # csv_reader is a iterartor
    next(csv_reader)  # use next function to don't print our headding 
    for data in csv_reader:
        print(data)
    