mfile = open("Somefile.txt") # open the file in reading only mode
content = mfile.read() #read the file content
#print(content) # print the file content

mfile = open("SomeFile2.txt", "w") # open the file in writing mode
content = mfile.write("bbbbbbbbbbbbbbbbbbb") #read the file content

mfile = open("SomeFile2.txt", "a") # open the file in append mode
content = mfile.write("aaaaaaaaaaaa") #read the file content

mfile.close() # close the file
