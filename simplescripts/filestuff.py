file=open("./mytextfile.txt", 'w')
file.write("This is a nice file")
file.close()

file=open("./mytextfile.txt", 'r')
fileContent=file.read()
print(fileContent)
file.close()

file=open("./mytextfile.txt", 'a')
file.write("\nthis is a new line")
file.close()

with open("./mysecondfile", 'w') as file:
    file.write("This is the first line")
# no need to close the file if we open it with "with"

