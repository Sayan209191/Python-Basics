# read a file and write another file ---->
# read from sal.txt file and write a new file contains -->
# Sayan's sallary is 100000
# chinmay's sallary is 50000



with open('sal.txt','r') as rf:
    with open('output.txt','a') as wf:
        for line in rf.readlines():
            name,sallary=line.split(',')
            wf.write(f"{name}\'s sallary is {sallary}")