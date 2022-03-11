import os
import shutil
path= "folder with text"
try:
   # os.remove(path) cannot delete empty folders
   # os.rmdir(path) #only deletes empty folders
    shutil.rmtree(path)
except FileNotFoundError:
    print("\nThe folder was not not not not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("you cannot delete that using that function")

else:
    print(path + " was deleted")





