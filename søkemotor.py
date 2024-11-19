import os #Needed to use clear terminal function
current_file = "tekstfil1.txt" #Sets current file to read

def print_menu():
    global current_file
    os.system('cls') #Clears the terminal

    print("")
    current_directory = os.getcwd() #Finds current path to files
    file_path = os.path.join(current_directory, current_file)
    if os.path.isfile(file_path):
        print("File found")
    else:
        print("File not found, reverted back to tekstfil1.txt")
        current_file = "tekstfil1.txt"
    print("")

    print("current selected file = " + current_file) #Prints which file is selected
    print("1. Search line")
    print("2. Search word")
    print("3. Change file")
    print("4. Create new txt file")

    choice = input("choose number from menu: ") #Choose option from list above by listening to 1,2 or 3.
    if choice == "1": #If choice 1, does call function underneath
        search_line() #Calls search line function
    elif choice == "2": #If choice 2, does call function underneath
        search_word() #Calls search word function
    elif choice == "3": #If choice 3, does call function underneath
        change_file() #Calls change filefunction
    elif choice == "4":
        create_name = input("Write name for your file. (Do NOT write '.txt' at the end): ")
        f = open(str(create_name) + ".txt", "w") #Creates a new name from the input. adds '.txt' at the end. "w" cant make a new one if already a file with that name exists.
        print("Succesfully created file. Changed current file to the new file")
        current_file = str(create_name) + ".txt" #Sets current file to the one created
        input("Press any key to exit")
        print_menu()
    else:
        print_menu() #If not any of options above, prints menu again


#Change current file
def change_file():
    os.system('cls') #Clears the terminal
    global current_file

    print("1. Change to tekstfil1.txt")
    print("2. Change to tekstfil2.txt")
    print("3. Change to tekstfil3.txt")
    print("4. Input custom txt file (Requires you to add your txt file in the folder)")
    choice = input("Choose which file to change to: ") #Input is your choice
    if choice == "1": #If your choice is 1 from list, does code underneath
        current_file = "tekstfil1.txt" #Changes current_file to be the string written
        print_menu()
    elif choice == "2": #If your choice is 2 from list, does code underneath
        current_file = "tekstfil2.txt" #Changes current_file to be the string written
        print_menu()
    elif choice == "3": #If your choice is 3 from list, does code underneath
        current_file = "tekstfil3.txt" #Changes current_file to be the string written
        print_menu()
    elif choice == "4":
        file_input = input("Write the name of the file (Do NOT write '.txt' at the end): ")
        current_file = file_input + ".txt"
        print(current_file)
        print_menu()
    else:
        change_file() #If none of options above, calls change_file function again


#Search for line in file
def search_line():
    os.system('cls') #Clears the terminal
    
    #Tekst file 1
    f = open(current_file, "r") #Open the current choosen file from the variable
    search = input("search line in file (Or leave empty to get the whole file text): ") #Input is your search

    for line in f:
        if search.lower() in line.lower(): #Checks for search in file lines. if found does code underneath
            print(line) #Prints the line with the word
    
    input("Press any key to exit: ")
    print_menu()


#Search for word in file
def search_word():
    os.system('cls') #Clears the terminal
    
    #Tekst file 1
    f = open(current_file, "r") #Open the current choosen file from the variable
    search = input("Search word in file: ") #Input is your search
    word_list = [] #Empty list of found searched words

    for line in f:
        if search.lower() in line.lower(): #Checks if search is in any line in the file
            word_list.append(search) #Adds each found search into the list
    print(word_list) #Prints list
    x = word_list.count(search) #Counts for search amount of times in list
    print("choosen word was found " + str(x) + " time(s)") #Prints amount of time search was found
    if word_list.count(search) >= 1: #If count in list equals 1 or more sets variable to true
        word_found = True
    else: #Else false
        word_found = False
    print("Word found = " + str(word_found)) #Prints out the variable
    
    input("Press any key to exit: ")
    print_menu()





print_menu() #Initially calls the function