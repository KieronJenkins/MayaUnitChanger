import maya.cmds as cmds

# Made using Python. This script changes the units in Maya between MM, CM and M

def change_maya_units():
    # cmds.currentUnit(linear = "millimeter") # For each different Popup Menu Item, delete a different # before cmds.currentUnit on only one line
    # cmds.currentUnit(linear = "centimeter")
    # cmds.currentUnit(linear = "meter")
    print("Units Changed") # Delete this if you don't want to print anything to console afterwards
    
    
change_maya_units()


# Set Up: Create a custom button in your shelf editor then Set to Python and then copy paste the above in as Popup Menu Items
