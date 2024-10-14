"""
    Author: Dan Shaw w0190983
    Title: Landscape Calculator
    Description: Computes the price of landscaping a new development based on plot width and depth, as well as grass type and tree count
"""

# Creates global level variables for all constant values
BASE_LABOUR = 1000
SURFACE_THRESHOLD = 5000
THRESHOLD_COST_MODIFIER = 500
TREE_COST = 100
GRASS_SQFT = ([ ["FESCUE", 0.05], 
                ["BENTGRASS", 0.02], 
                ["CAMPUS", 0.01] ])

def main():
    greeting = "| Landscaping Cost Calculator |"

    # Outputs the greeting banner to the user
    print("-" * len(greeting))
    print(greeting)
    print("-" * len(greeting))

    # Gets user input, validates within functions
    houseNumber = getHouseNumber()
    propDimensions = [ getPropDimension(0), getPropDimension(1) ]
    grassType = getGrassType()
    treeCount = getTreeCount()

    # Performs calculations
    totalCost = getTotalCost(propDimensions, treeCount, grassType)
    print(totalCost)

# Gets and validates the type of grass from the user
def getGrassType():
    global GRASS_SQFT
    i = 0
    print("Enter the number that corresponds to the desired grass type.")
    
    # Iterates through GRASS_SQFT and outputs the grass type along with its index
    for grassType in GRASS_SQFT:
        print("\t({0}) {1}".format(i + 1, grassType[0])) # Add 1 to account for 0-indexing
        i += 1
    
    # Gets and validates the type of grass from the user
    while (index := validateGrassInput(input("> "))) == None:
        print("Invalid input. Please enter a valid grass type.")
    
    # Subtracts 1 to get back to 0-indexing
    index -= 1

    # Outputs the selected grass type
    print("You have selected {0} grass.".format(GRASS_SQFT[index][0].capitalize()))
    return index

# Calculate the total cost of the landscaping based on propDimensions, treeCount, and grassType
def getTotalCost(propDimensions, treeCount, grassType):
    # Get access to global variables
    global BASE_LABOUR, SURFACE_THRESHOLD, THRESHOLD_COST_MODIFIER, TREE_COST, GRASS_SQFT

    # Calculates the property area
    propertyArea = int(propDimensions[0]) * int(propDimensions[1]) 

    # Calculate the total cost and, if the property area is greater than the SURFACE_THRESHOLD, add the THRESHOLD_COST_MODIFIER
    totalCost = BASE_LABOUR + (propertyArea * GRASS_SQFT[grassType][1]) + (treeCount * TREE_COST)
    if propertyArea > SURFACE_THRESHOLD:
        totalCost += THRESHOLD_COST_MODIFIER

    return totalCost

# NOTE I spent so long trying to figure out why this function actually works because converting a decimal number to an int shouldn't throw an exception at all, then I realized trying to convert a STRING with a decimal to an int will throw a ValueError
# Attempts to convert value to int. If successful, returns the converted value
# If fails, returns None
def validateInt(value):
    try:
        return int(value)
    except ValueError:
        return None

# Gets the desired number of trees from the user and validates input
def getTreeCount():
    while (treeCount := validateInt(input("Enter the number of trees desired.\n> "))) == None:
        print("Invalid input. Please enter a valid number of trees.")
    return treeCount

# Returns converted value if inputString is in validInput list
# Returns None if inputString is not in validInput list
def validateGrassInput(inputString):
    validInput = getValidInputs()
    if inputString not in validInput:
        return None
    
    return int(inputString)

# Gets the length of GRASS_SQFT and populates validInput with the indices
def getValidInputs():
    validInput = []
    for i in range(len(GRASS_SQFT)):
        validInput.append(str(i + 1))
    return validInput

# Gets and validates property dimensions
# axis == 0 -> depth
# axis == 1 -> width
def getPropDimension(axis):
    if axis == 0:
        while (propDimension := validateInt(input("Enter property depth in feet.\n> "))) == None:
            print("Invalid input. Please enter a valid property depth.")
        return propDimension
    elif axis == 1:
        while (propDimension := validateInt(input("Enter property width in feet.\n> "))) == None:
            print("Invalid input. Please enter a valid property width.")
        return propDimension

# Gets and validates house number
def getHouseNumber():
    while (houseNumber := validateInt(input("Enter Your House Number.\n> "))) == None:
        print("Invalid input. Please enter a valid house number.")
    return houseNumber

if __name__ == "__main__":
    main()