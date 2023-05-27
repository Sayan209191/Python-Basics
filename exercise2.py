# read a html file ---> read all the url from this html file
# write those url in a text file



# with open('exercise2.html','r') as webpage:
#     with open('Output2.txt','a') as  wf:
#         for line in webpage.readlines():
#             if '<a href=' in line:
#                 pos=line.find('<a href=')
#                 first_cout=line.find('\"',pos)
#                 second_cout=line.find('\"',first_cout+1)
#                 url=line[first_cout+1:second_cout]
#                 wf.write(f"{url}\n")



# another and best  solution ---->


with open('exercise2.html','r') as webpage:
    with open('output2.txt','a') as wf:
        page=webpage.read()
        link_exit=True
        while link_exit:
            pos=page.find('<a href=')
            if pos==-1:
                link_exit=False
            else:
                first_cout=page.find('\"',pos)
                second_cout=page.find('\"',first_cout+1)
                url=page[first_cout+1:second_cout]
                wf.write(f"{url}\n")
                page=page[second_cout:]
                    