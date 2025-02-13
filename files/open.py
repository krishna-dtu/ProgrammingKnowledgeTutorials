#<file_handle>=open(<file_name>,<mode>)
f=open("sample.txt")
#3 basic functions to read the data from the file
# 1) read function 
# 2) readline function
# 3) readlines function
print(f.readlines())

f.close()