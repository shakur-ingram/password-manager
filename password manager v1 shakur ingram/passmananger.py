# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    ''' Displays an Options Menu. You will need to update this code so that this section is replaced
    by the printing of a single global variable called 'menu' which has been assigned a multi line string that contains your 
    options menu. You will need to declare the variable in the same place as the 'choice' variable'''
    print("\n   Password Manager Menu   \n")
    print("\n[1] To add credentials")
    print("[2] To view credentials")
    print("[q] Enter q to quit")
    
    # Ask for the user's choice.
    choice = input("\nMake your choice: ")
    
    # Respond to the user's choice. You will need to ammend this section to reflect the menu requirements of the assessment
    if choice == '1':
        url = input("\nenter url: ")        
        usern = input("\nEnter username: ")
        password = input("\nenter password: ")
        
        charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
        encpassword = "".join([charSet[(charSet.find(c)+3)%95] for c in password])
        encurl = "".join([charSet[(charSet.find(c)+3)%95] for c in url])
        encusern = "".join([charSet[(charSet.find(c)+3)%95] for c in usern])
        f = open("file.txt", "a")
        f.write(encurl + "   " + encusern + "   " + encpassword + "   1")

        print("\nYour new details have now been stored\n")

    elif choice == '2':
        f = open("file.txt", "r")
        data = f.read() # 'data' now contains the contents of the file as a string
        if data != "":
         print("yes there's data")
         stripped_data = data.strip() # data2 has now been strippped of any leading or trailing white spaces
         dataList = stripped_data.split("  ") # split string into a list with 2 spaces as the default delimiter
        i = 0
        border = "|"
        print(f"{border}{'URL' : ^20}{border}{'User' : ^20}{border}{'Password' : ^20}{border}")
        print("----------------------------------------------------------------")
        while i < len(dataList): #repeat until 'i' is larger than the list length
            print(f"{border}{dataList[i] : ^20}{border}{dataList[i+1] : ^20}{border}{dataList[i+2] : ^20}{border}")   
            i += 3
        else:
            print("\nAll data has now been displayed\n")
    elif choice == 'q':
        print("\nExiting the menu\n")
    else:
        print("\nInvalid option, please try again.\n")
        
# Print a message that we are all finished.
print("Program exit.")