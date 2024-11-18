f = open("tekstfil1.txt")
search = input("søk etter linje: ")

for line in f:
    if search in line:
        print(line)