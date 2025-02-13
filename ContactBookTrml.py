# =================================== Contact book in Terminal =====================================

# -------------- Constants ------------------
FILEPATH = "ContactsBook.txt"

# -------------- Functions ------------------
def fetchData():
    global contactDict
    contactDict = {}
    with open(FILEPATH, "r") as fp:
        line = fp.readline()
        while line != "":
            cont = line.split(" : ")
            contactDict.update({cont[0]:cont[1][0:-1]})
            line = fp.readline()
        fp.close()
    
def writeData():
    with open(FILEPATH, "w") as fp:
        for key in contactDict.keys():
            fp.write(f"{key} : {contactDict[key]}\n")
        fp.close()


choice = ""
times = 0

while (choice != "0"):

    times += 1
    print(f'''======================[{times}]== PHONE CONTACT BOOK ==[{times}]==============================\n
          0 : Exit
          1 : Add Contacts
          2 : Delete a contact
          3 : Search contact by name
          4 : Sort Contact list
          5 : Display Contact List
          6 : Display list with starting charecter
          7 : Edit Contact
          8 : Delete Phone Book
          ''')
    
    try:
        print("\n----------------------------------------------------\n")
        choice = input("Choose an option as you want from (0/1/2/3/4/5/6/7/8): ")
        if int(choice) == 0:
            print("Boyyyyyyyeeee...!")
            exit()
    except Exception as e:
        print(f"Try again, The error is : {e}")

# ----------------- [1] Add Contact ---------------------

    if choice == "1":
        try:
            print("\n+++++++++++ So you want to add phone numbers ++++++++++++++\n")
            print("---> Add numbers here...\n")
            nameList = []
            numberList = []
            for i in range(int(input("How many contacts do you want to add: "))):
                name = input(f"\n{i+1}) Enter name of the contact: ")
                while not len(name):
                    name = input(f"\n{i+1}) Enter name of the contact: ")
                nameList.append(name)
                mobileNum = ""
                while len(mobileNum) > 10 or len(mobileNum) < 10:
                    mobileNum = input(f"Enter the phone number: ")
                numberList.append(mobileNum)
            
            for k in range(len(nameList)):
                contact = nameList[k]+" : "+numberList[k]
                with open(FILEPATH, "a") as f:
                    f.write(f"{contact}")
                    f.write("\n")
            print("Contact/s added Successfully!")
        except Exception as e:
            print("Invalid Option! Try Again!")

    elif choice == "2":
        try:
            print("+++++++++++++ So you want to delete phone numbers +++++++++++++++\n")
            print("1 : Delete contact with NAME\n2 : Delete contact with NUMBER\n\n")
            select  = input("Choose an option (1/2): ")
            while select not in ["1", "2"]:
                select = input("Choose an option (1/2): ")
            
            if select == "1":
                delName = input("Enter the name here: ")
                contactDict = {}
                temp = ""
                with open(FILEPATH, "r") as fp:
                    line = fp.readline()
                    while line != "":
                        cont = line.split(" : ")
                        if cont[0] != delName:
                            contactDict.update({cont[0]:cont[1][0:-1]})
                        else:
                            temp = cont[0]
                            #break
                        line = fp.readline()
                        
                    fp.close()
                if delName not in contactDict.keys() and delName != temp:
                    print(f"{delName} not found! Please try again!")
                else:
                    with open(FILEPATH, "w") as fp:
                        for key in contactDict.keys():
                            fp.write(f"{key} : {contactDict[key]}\n")
                        print(f"{delName} has been deleted!")
                        fp.close()
            else:
                delNum = input("Enter the number here: ")
                contactDict = {}
                temp = ""
                with open(FILEPATH, "r") as fp:
                    line = fp.readline()
                    while line != "":
                        cont = line.split(" : ")
                        if cont[1][0:-1] != delNum:
                            contactDict.update({cont[0]:cont[1][0:-1]})
                        else:
                            temp = cont[1][0:-1]
                            #break
                        line = fp.readline()
                        
                    fp.close()

                if delNum not in contactDict.values() and delName != temp:
                    print(f"{delNum} not found! Please try again!")
                else:
                    with open(FILEPATH, "w") as fp:
                        for key in contactDict.keys():
                            fp.write(f"{key} : {contactDict[key]}\n")
                        print(f"{delNum} has been deleted!")
                        fp.close()
        
        except Exception as e:
            print("Invalid Option! Try Again!")

    elif choice == "3":
        print("\n++++++++++++++++ So you want to Search phone numbers +++++++++++++++\n")
        print("1 : Get number by NAME\n2 : Get name by NUMBER\n\n")
        select = input("Select an option as (1/2): ")
        while select not in ["1", "2"]:
            select = input("Select an option as (1/2): ")
        
        if select == "1":
            searchNum = input("Enter name of contact to get number: ")
            while not len(searchNum):
                searchNum = input("Enter name of contact to get number: ")
            flag = 0
            fetchData()

            for key in contactDict.keys():
                if key == searchNum:
                    print(f"{key}:{contactDict[key]}")
                    flag = 1
                    break
            
            if not flag: print(f"{searchNum} Not Found!")

        else:
            searchName = input("Enter number of contact to get name: ")
            while not len(searchName):
                searchNum = input("Enter number of contact to get name: ")
            flag = 0
            fetchData()

            for key in contactDict.keys():
                if contactDict[key] == searchName:
                    print(f"{key}:{contactDict[key]}")
                    flag = 1
                    break
            if not flag: print(f"{searchName} Not Found!")
        
    elif choice == "4":
        fetchData()

        sort = sorted(contactDict)
        with open(FILEPATH, "w") as fp:
            for key in sort:
                fp.write(f"{key} : {contactDict[key]}\n")
            fp.close()
        print("Phone Book Sorted Successfull!")

    elif choice == "5":
        count = 1
        print("\n------------------ Contact Info ----------------------\n")
        with open(FILEPATH, "r") as fp:
            line = fp.readline()
            if (line == ""): print("Phone book is empty!")
            else:
                while line != "":
                    print(f"{count}) {line}")
                    count += 1
                    line = fp.readline()
                fp.close()

    elif choice == "6":
        print("\n----------------------------- Display contact list with given charecter --------------------\n")
        fetchData()
        flag = 0
        char = input("Enter a charecter to get contacts: ").lower()
        for key in contactDict.keys():
            if str(key).lower().startswith(char):
                print(f"{key} : {contactDict[key]}")
                flag = 1
        if flag == 0:
            print(f"Contacts with charecter {char} doesn't exist!")
    
    elif choice == "7":
        print("\n-------------------- Edit contact here ---------------------\n\n")
        print("1 : Enter name to edit NUMBER\n2 : Enter number to edit NAME: ")
        select = input("Choose an option as you want (1/2): ")
        while select not in ["1","2"]:
            select = input("Choose an option as you want (1/2): ")
        
        if select == "1":
            name = input("Enter name here to edit number: ").capitalize()
            flag = 0
            while not len(name):
                name = input("Enter name here to edit number: ").capitalize()
            fetchData()
            for key in contactDict.keys():
                if key == name:
                    flag = 1
                    newNum = input(f"Enter new number\n{name}: ")
                    while len(newNum) != 10:
                        print("ERROR! NUMBER LENGTH MUST BE 10")
                        newNum = input(f"Enter new number\n{name}: ")
                    contactDict[key] = newNum
                    writeData()
                    break
            if flag == 0:
                print(f"{name} doesn't exist! try again!")

        else:
            number = input("Enter number here to edit name: ")
            flag = 0
            while len(number) != 10:
                print("ERROR! NUMBER LENGTH MUST BE 10")
                number = input("Enter number here to edit name: ")
            fetchData()
            for key in contactDict.keys():
                if contactDict[key] == number:
                    flag = 1
                    newName = input(f"Enter new name for number {number}: ")
                    key = newName # need to be debugged...
                    writeData()
                    break
            if flag == 0: print(f"{number} doesn't exist! try again!")
        

    elif choice == "8":
        checkAgain = input("Are you sure you wanna delete the phone book (y/n): ").lower()
        if checkAgain not in ["y","yes"]:
            pass
        else: 
            with open(FILEPATH, "w") as fp:
                fp.write("")
                fp.close()
            print("Phone booke deleted!")
    
    else:
        print("Invalid option! Try Again!")