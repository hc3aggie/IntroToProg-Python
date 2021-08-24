# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# RRoot 1/1/19
# ChangeLog (HChisolm, 8/22/2021, Editing to a dictionary):
# HChisolm, 8/22/2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile= "ToDoList.txt"   # An object that represents a file
objFile = None
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection

strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
# creating a table in ToDoList.txt that will start with values so we already have data here.
dicRow = {"Task":"Pay Bills", "Priority":"High"}
lstTable.append(dicRow)
dicRow = {"Task":"Pick Up Dry Cleaning", "Priority":"Medium"}
lstTable.append(dicRow)
dicRow = {"Task":"Go to the Post Office", "Priority":"Low" }
lstTable.append(dicRow)
# Write to text file
objFile = open(strFile, "w")
for row in lstTable:
    objFile.write(row["Task"] + "," + row["Priority"] + "\n")
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()
    # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        objFile = open(strFile, "r")
        for row in objFile:
            strData = row.split(",")
            dicRow = {"Task": strData[0], "Priority": strData[1].strip()}

        for item in lstTable:
            print(item)
        objFile.close()
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task= input("Enter a Task:")
        priority = input("Enter a priority (High, Medium or Low):")
        #categorizing our priorities for dictionary entries.
        # have to make each priority seperately ==
        dicRow = {"Task": task, "Priority": priority}
        objFile = open(strFile, "a")
        objFile.write(dicRow["Task"] + ", " + dicRow["Priority"] + "\n")
        objFile.flush
            #saving current data to be brought up
        objFile.close()
        print("Input Saved to File")

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        remove = input("Which task would you like to remove?")
        # open file to read each row and append to list if not selected for removal
        objFile = open(strFile, "r")
        for row in objFile:
            strData = row.split(",")
            if remove == strData[1].strip():
        objFile.close()
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for item in lstTable:
            objFile.write(item["Task"] + ", " + item["Priority"] + "\n")
        objFile.close()
        input("Data has been saved to file. Press enter to return to menu")
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Press enter to exit")
        break
        # and Exit the program
