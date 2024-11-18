import os
current_file = "tekstfil1.txt"

def print_menu():
    os.system('cls')
    print("current selected file = " + current_file)
    print("1. Search line")
    print("2. Search word")
    print("3. Change file")
    choice = input("choose number from menu: ")
    if choice == "1":
        search_line()
    elif choice == "2":
        search_word()
    elif choice == "3":
        change_file()
    else:
        print_menu()


#Change current file
def change_file():
    os.system('cls')
    global current_file

    print("1. Change to tekstfil1.txt")
    print("2. Change to tekstfil2.txt")
    print("3. Change to tekstfil3.txt")
    choice = input("Choose which file to change to: ")
    if choice == "1":
        current_file = "tekstfil1.txt"
        print_menu()
    elif choice == "2":
        current_file = "tekstfil2.txt"
        print_menu()
    elif choice == "3":
        current_file = "tekstfil3.txt"
        print_menu()
    else:
        change_file()


#Search for line in file
def search_line():
    os.system('cls')
    
    #Tekst file 1
    f = open(current_file, "r")
    search = input("search line in file: ")

    for line in f:
        if search in line:
            print(line)
    
    input("Press any key to exit: ")
    print_menu()


#Search for word in file
def search_word():
    os.system('cls')
    
    #Tekst file 1
    f = open(current_file, "r")
    search = input("Search word in file: ")
    word_list = [] #Empty list of found searched words

    for line in f:
        if search in line: #Checks if search is in any line in the file
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





print_menu()