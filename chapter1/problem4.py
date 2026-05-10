import os

# specify directory path
path = "/"

# get list of files and directories
contents = os.listdir(path)

# print contents
print("Contents of directory:")
for item in contents:
    print(item)