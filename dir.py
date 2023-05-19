#Import os module
import os

#Initialize the directory name
dirname = "MyDir"
#Check the directory name exist or not
if os.path.isdir(dirname) == False:
    #Create the directory
    os.mkdir(dirname)
    #Print success message
    print("The directory is created.")
else:
    #Print the message if the directory exists
    print("The directory already exists.")
