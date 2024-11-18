import os

def print_menu():
    os.system('cls')
    print("1. Search line")
    print("2. Search word")
    print("3. Change file (Not implemented)")
    choice = input("choose number from menu: ")
    if choice == "1":
        search_line()
    elif choice == "2":
        search_word()
    else:
        print_menu()



def search_line():
    os.system('cls')
    f = open("tekstfil1.txt", "r")
    search = input("search line in file: ")

    for line in f:
        if search in line:
            print(line)
    
    input("Press any key to exit: ")
    print_menu()

def search_word():
    os.system('cls')
    f = open("tekstfil1.txt", "r")
    search = input("Search word in file: ")
    word_list = []

    for line in f:
        if search in line:
            word_list.append(search)
    print(word_list)
    x = word_list.count(search)
    print("choosen word was found " + str(x) + " time(s)")
    
    input("Press any key to exit: ")
    print_menu()


print_menu()