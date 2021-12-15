""" 
    Brittany Normandin for assignment module WhatABook
    Class: CSD 310
    Date: December 10, 2021
"""
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

""" DISPLAY MAIN MENU """
def displayMenu():

    print("\n --What A BooK Menu--\n")
    print("\n   1. Store locations\n   2. Book List\n   3. My Account\n   4. Exit\n")

    # Array of valid Main Menu Selections
    mainMenuOptions = ["1", "2", "3", "4"]

    # Take in the users choice of Main Menu Options
    choice = input(" Please make a selection based on the number. ")
    
    # If the user inputs anything other than a valid Main Menu Option the user will be re-prompted
    while choice not in mainMenuOptions:
        print("\n Invalid Selection: Please try picking one of the menu options below.")
        print("\n  1. Store locations\n   2. Book List\n   3. My Account\n   4. Exit\n")
        choice = input(" Please make a selection based on the number. ")

    # Checks if Main Menu selection is valid and stores it as an int and returns it 
    if choice in mainMenuOptions:
        validChoice = int(choice)
        return validChoice
    
""" DISPLAY STORE LOCATIONS """
def displayLocations(_cursor):

    # Grabbing store locations from database
    _cursor.execute("SELECT store_id, locale FROM store")
    stores = _cursor.fetchall()

    # Printing store locations with for loop in stores
    print("\n --Current Store Locations-- \n")
    for i in stores:
        print(f" Location: {i[1]}\n")

""" DISPLAY BOOK LISTINGS """
def displayBooks(_cursor):

    # Grabbing the books from database
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = _cursor.fetchall()

    # Printing the books in database with for loop in books
    print("\n --Book List-- \n")
    for i in books:
        print("\n  Book ID: {}\n  Book Name: {}\n  Details: {}\n  Author: {}\n".format(i[0], i[1], i[2], i[3]))

""" VALIDATE USER ACCOUNT """
def validateUser():

    print("\n --Account Login-- \n")

    # Array of valid User IDs
    validUserIds = ["1", "2", "3"]

    # Storing user input for checking a valid USER ID
    userID = input("Please enter your user ID: ")

    # Checking if user inputs an invalid USER ID and re-prompts user
    while userID not in validUserIds:
        print("\n** User ID is no valid, please try again. **\n")
        userID = input("Please enter your user ID: ")
    # Checks if there is a valid USER ID and converts it to an int and returns it
    if userID in validUserIds:
        validUserID = int(userID)
        return userID

""" DISPLAYING USER ACCOUNT MENU """
def displayAccountMenu():

    print("\n --Account Menu-- \n")
    print("\n 1. Wishlist\n 2. Add to Wishlist\n 3. Main Menu\n 4. Exit program")

    # Array of valid Account Options
    validAccountOptions = ["1", "2", "3", "4"]

    # Storing users selection of account menu
    accountOptions = input("\n Please enter a valid menu option. ")

    # Checking user input for account main menu and re-prompting if user enters and invlaid selection
    while accountOptions not in validAccountOptions:
        print("\n** Selection is not valid: Please pick a menu option.")
        accountOptions = input("\n Please enter a valid menu option. ")
    
    # Checks for valid account menu option and converts it to an int and returns it
    if accountOptions in validAccountOptions:
        validAccountOption = int(accountOptions)
        return validAccountOption

""" DISPLAY BOOKS THAT CAN BE ADDED TO WISHLIST """
def displayBooksToAdd(_cursor, _user_id):

    # Creating mySQL query to grab available books 
    availableBooks = ("SELECT book_id, book_name, author, details FROM book " +
                    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    # Executing query                 
    _cursor.execute(availableBooks)

    # Storing the query results of books that  are available to be added to wishlist
    bookstoAdd = _cursor.fetchall()

    # Printing the books that can be added
    print("\n --Available Books-- ")
    for i in bookstoAdd:
        print(f"\n Book ID: {i[0]}\n Book Name: {i[1]}\n")
    
""" ADDING BOOK TO WISHLIST METHOD """
def addBookToWishlist(_cursor, _user_id, _book_id):

    # Executing mySQL query to add a book to wishlist of user
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, addBookID))

""" DISPLAY USER WISHLIST """
def displayWishlist(_cursor, _user_id):

    # Executing mySQL query to access wishlist books with INNER JOIN
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    # Grabbing and storing wishlist books from query
    wishlist = _cursor.fetchall()

    # Printing wishlist books of user
    print("\n --Display Wishlist-- ")
    for book in wishlist:
        print("     Book Name: {}\n     Author: {}\n".format(book[4], book[5]))

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the whatabook database 
    
    cursor = db.cursor()

    print("\n Welcome to WhatABook Application! ")

    # Storing display menu method return value in a variable for use in while loop
    mainMenuSelection = displayMenu()

    # Running program while mainMenuSelection is a proper user selection from Main Menu
    while mainMenuSelection < 4:
        # Main Menu selection 1 displays stores in database
        if mainMenuSelection == 1:
            displayLocations(cursor) 
        # Main Menu selection 2 displays store locations         
        if mainMenuSelection == 2:
            displayBooks(cursor)
        # Main Menu selection 3 validates user ID and enters user account menu           
        if mainMenuSelection == 3:
            myID = validateUser()
            # Storing user input selection on Account Main Menu
            accountOption = displayAccountMenu()
            # While loop runs and checks user input. if user selection equals 3 it returns them to 
            # the Main Menu
            while accountOption != 3:
                # Account Menu selection 1 displays user wishlist
                if accountOption == 1:
                    displayWishlist(cursor, myID)
                # Account Menu selection 2 displays books that can be added to wishlist and asks
                # user to input book ID they wish to add to their wishlist and then commits that book to 
                # the database                           
                if accountOption == 2:
                    displayBooksToAdd(cursor, myID)
                    addBookID = input("\n Enter the ID of the book to add: ")
                    validBookID = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    while addBookID not in validBookID:
                        print("\n** Invlaid Book ID. Please try again! **")
                        addBookID = input("\n Enter the ID of the book to add: ")
                    if addBookID in validBookID:
                        validBookID = int(addBookID)
                    addBookToWishlist(cursor, myID, validBookID)
                    db.commit()
                    print("\n The book was added to the wishlist!")
                # Account Menu selection 4 terminates program
                if accountOption == 4:
                    print("\n\n Program ending, closing...")
                    sys.exit()
                accountOption = displayAccountMenu()
            
        mainMenuSelection = displayMenu()
        # Main Menu selection 4 terminates the program
        if mainMenuSelection == 4:
            print("\n\n Program ending, closing...")
            sys.exit()
      

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password is incorrect.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The database you are looking for does not exist.")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()
