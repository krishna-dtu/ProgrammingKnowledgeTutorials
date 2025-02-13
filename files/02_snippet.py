f=open("sample.txt")
b=0
lines=0
for i in f.read():
    b+=1
print("no. of bytes in the file is ",b)
f.close()
f=open("sample.txt")
for i in f.readlines():
    lines+=1
print("No. of lines in the file is ",lines)