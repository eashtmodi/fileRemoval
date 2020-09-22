# this program deletes files and backups them if they are there for more than 1 min
import os
import shutil
import time

print("Please enter your name: ")
nameP=input()
welcomeString="Welcome {}".format(nameP)
print(welcomeString)
print("Please enter the name or path of file you want to remove")
removalFolderName=input()


# defining the path of both files
path=removalFolderName
days=30

initialTime=time.time()-(days*24*60*60)

if os.path.exists(path):
    print(os.listdir(path))
    for()
        cTime=time.time()
        if(cTime-initialTime>=60):
            for file1 in removalPath:
                name,ext=os.path.splitext(file1)        
                newPath= os.path.join(path+"/"+name)
                os.remove(newPath)

input("Enter To Exit")



    

