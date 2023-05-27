# csv file read by using DictReader   ---->


from csv import DictReader
from unicodedata import name
with open('file1.csv','r') as f:
    csv_reader=DictReader(f)
    for row in csv_reader:
        # print(row)
        print(row['Name'])   # print name , similarly we can read any thing from csv file