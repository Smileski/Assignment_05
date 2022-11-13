#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# LSmileski, 2022-Nov-12, Edited File
# LSmileski, 2022-Nov-13, Edited File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lisRow = {}  # dictionary of data row
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('\nThe Magic CD Inventory\n')
while True:
    
#  Display menu allowing the user to choose:
    print('[a] Add CD\n[i] Display Current Inventory\n[d] Delete CD from Inventory')
    print('[s] Save Inventory to file\n[l] Load Inventory from file\n[x] Exit')
    strChoice = input('a, i, d, s, l or x: ').lower()  # convert choice to lower case at time of input
    print()

# 6. Exit the program if the user chooses so
    if strChoice == 'x':      
        break
 
# 1. Add data to the table (2d-list) each time the user wants to add data
    if strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        intID = int(input('Enter an ID: '))
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'id': intID,'title': strTitle,'artist': strArtist}
        lstTbl.append(dicRow)

# 2. Display the current data to the user each time the user wants to display the data      
    elif strChoice == 'i':
        print('ID, CD Title, Artist')
        for row in lstTbl:
                print(str(row['id']) + ',\t' + row['title'] + ',\t' + row['artist'] + '\n')
        print('\n Displayed current Invetory! \n') 

# 3. Delete CD from Inventory            
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        deleteId = int(input('Enter id that would love to delete'))
        # using del + loop, deleting dictionary in list
        for row in range(len(lstTbl)):
            if lstTbl[row]['id'] == deleteId:
                del lstTbl[row]
                break
        print('\n The dictionary is successfully deleted! \n')
 
# 4. Save the data to a text file CDInventory.txt if the user chooses so 
    elif strChoice == 's': 
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            objFile.write(str(row['id']) + ',' + row['title'] + ',' + row['artist'] + '\n')
        objFile.close()
        print('\n Saved inventory to a file! \n') 
        
# 5. Load inventory from a file (read from a file)
    elif strChoice == 'l':
    # TODO Add the functionality of loading existing data
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id': lstRow[0], 'title': lstRow[1], 'artist':lstRow[2]}
            lstTbl.append(dicRow)
            #print(dicRow)
        objFile.close()
        print('ID, CD Title, Artist')
        for row in lstTbl:
                print(str(row['id']) + ',\t' + row['title'] + ',\t' + row['artist'] + '\n')
        
    else:
        print('Not a valid choice! Please choose either a, i, d, s, l or x!')

