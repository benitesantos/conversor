
import sys

from PyQt5. QtWidgets import *

# Declare the class to create combobox by using list data

class ComboExample (QMainWindow ):

    def __init__ ( self ):

        super ( ). __init__ ( )


        # Set the tittle of the window

        self. setWindowTitle ( "ComboBox with List data " )

        # Set the geometry for the window

        self. setGeometry ( 100 , 100 , 350 , 150 )


        # Create combobox

        self. combobox = QComboBox ( self )

        # Set the geometry for the combobox

        self. combobox. setGeometry ( 30 , 30 , 200 , 30 )


        # Define list items for the combobox

        src_engines = [ "google.com" , "yahoo.com" , "ask.com" , "baidu.com" , "yandex.com" ]

        # Enable the editable option of the combobox

        self. combobox. setEditable ( True )

        # Set the first item for the combobox

        self. combobox. addItem ( "Select Search Engine" )

        # Add multiple items in the combobox using list

        self. combobox. addItems (src_engines )


        # Define label at the bottom of the combobox to provide message for the user

        self. msgLabel = QLabel ( '' , self )

        # Set the geometry for the label

        self. msgLabel. setGeometry ( 30 , 60 , 290 , 60 )


        # Call the custom function when any item is selected

        self. combobox. activated [ str ]. connect ( self. onClicked )


        # Move the position of the window

        self. move ( 800 , 400 )

        # Display the Window

        self. show ( )


    # Define a method to handle the click event of the Combobox

    def onClicked ( self , val ):

        # Check any item is selected by the user or not

        if val == "Select Search Engine":

            message = "You have selected nothing."

        else:

            message = "Your favorite search engine is " + val


        # Display the message text in the label

        self. msgLabel. setText (message )

        # Display the message in the console

        print (message )


# Create the app object

app = QApplication ( sys. argv )

# Create an object of the class object

combo = ComboExample ( )

# Execute the app

app. exec ( )