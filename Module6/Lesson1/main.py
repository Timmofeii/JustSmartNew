import  os


file_name = "FILE_name"





with open(file_name,'r') as file:
    lines = file.readlines()
    for line in range(len(lines)):
        if "by" in lines[line]:
            print(lines[line])


