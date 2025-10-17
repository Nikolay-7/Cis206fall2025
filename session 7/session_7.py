#opens and reads the names file
file = open('names.txt', 'r')
names = file.read().lower()
file.close()

#Open the nofound file for writinng
output_file = open('nofound.txt', 'w')

#loop to keep asking names
while True:
    name = input("Enter a name (or type 'q' to quit): ")
    
    if name == 'q':
        break
    
    #checks if name is in the file
    if name.lower() in names:
        print("The name '" + name + "' is already in the file names.")
    else:
        output_file.write(name + '\n')
        print("The name '" + name + "' has been written to nofound.txt.")

#closes the nofound file
output_file.close()