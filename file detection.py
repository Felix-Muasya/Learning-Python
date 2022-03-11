import os
path = "C:\\Users\\USER\\Desktop\\New folder"
if os.path.exists(path):
    print("location Exists")
    if os.path.isfile(path):
        print("The location holds a file")
    elif os.path.isdir(path):
        print("the location holds a directory")
    elif os.path.islink(path):
        print("Location is a link")
    else:
        print("location exists but holds unknown thing")
else:
    print("location does not exist")





