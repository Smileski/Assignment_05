#------------------------------------------#
# Title: CDInventory.py
# Desc: Script CDINventory to store CD Inventory data
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# LjSmileski, 2022-Nov-06, Created Code
#------------------------------------------#

# 1. Display menu allowing the user to choose: 'Add CD', 'Display Current Inventory', 'Save Inventory to file' and 'exit'
listTable = [] #declaring empty list
ans = True
while ans:

    print (' Menu\n','1.Add CD\n','2.Display Current Inventory\n','3.Save Inventory to file\n','4.Exit' )
    ans=input('What would you like to do? ')
    
# 2. Add data to the table (2d-list) each time the user wants to add data
    if ans=='1': 
      newID = input('Enter an ID: ')   
      cdTitle = input('Enter CD title: ')  
      artistName = input('Enter artist name: ')
      addData = [newID, cdTitle, artistName] #adding data into the list
      listTable.append(addData) #every entered row of data saves into new list
      print('\n CD added \n') 
      
# 3. Display the current data to the user each time the user wants to display the data
    elif ans=='2':
      print ('ID\t', 'CD Title\t', 'Artist Name\t', sep='|\t')
      for row in listTable:
          for itemInRow in row:
              print(itemInRow, '|\t', end = '\t\t')
          print()
      print('\n Displayed current Invetory! \n') 
      
# 4. Save the data to a text file CDInventory.txt if the user chooses so
    elif ans=='3':
      strRow = ''
      cdInventory = open('CDInventory.txt', 'w')
      for row in listTable:
          for itemInRow in row:
              strRow += str(itemInRow) + ', '
          strRow = strRow[:-1] + '\n'
      cdInventory.write(strRow + '\t')
      cdInventory.close()
      print('\n Saved inventory to a file! \n') 
      
# 5. Exit the program if the user chooses so.
    elif ans=='4':
       print('\n You choose to exit! Goodbye') 
       break
    elif ans !='':
       print('\n Not a valid choice, pleace try again! \n') 
       

            

    




    
