import os
current_file = "tekstfil1.txt"

def add(a, b):
    return a + b

print(add(2, 3))

'''def search_word():
    os.system('cls') #Clears the terminal
    
    #Tekst file 1
    f = open(current_file, "r") #Open the current choosen file from the variable
    search = input("Search word in file: ") #Input is your search
    word_list = [] #Empty list of found searched words

    for line in f:
        if search.lower() in line.lower(): #Checks if search is in any line in the file
            word_list.append(search) #Adds each found search into the list
    x = word_list.count(search) #Counts for search amount of times in list
    #print("choosen word was found " + str(x) + " time(s)") #Prints amount of time search was found
    if word_list.count(search) >= 1: #If count in list equals 1 or more sets variable to true
        word_found = True
    else: #Else false
        word_found = False
    #print("Word found = " + str(word_found)) #Prints out the variable

    
    f.close
    return [search, word_found, x]'''



#result = search_word()
#print(result)
#print("ordet ble funnet: " + str(result[2]) + " ganger")


def search_line():
    os.system('cls') #Clears the terminal

    
    #Tekst file 1
    f = open(current_file, "r") #Open the current choosen file from the variable
    search = input("search line in file (Or leave empty to get the whole file text): ") #Input is your search
    print(" ")
    
    for line in f:
        if search.lower() in line.lower(): #Checks for search in file lines. if found does code underneath
            print(line) #Prints the line with the word


search_line()