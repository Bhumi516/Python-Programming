# Directories
# rename, change, remove, list


# Create a directory

# import os
# os.mkdir("Test")
# print("Directory created successfully")



#List Directory 

# import os
# files = os.listdir(".")
# for file in files:
#     print(file)



# Change Directory

# import os
# os.chdir("Test")
# print("Current directory:", os.getcwd())




# rename directory

# import os
# os.rename("Test", "Bhumi")
# print("Directory renamed successfully")




# remove 

# import os
# os.rmdir("Bhumi")
# print("Directory removed successfully")




# directory exist or not

import os
if os.path.exists("Bhumi"):
    print("Directory exists")
else:
    print("Directory does not exist")