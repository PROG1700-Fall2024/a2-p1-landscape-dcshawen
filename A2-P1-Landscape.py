"""
    Author: Dan Shaw w0190983
    Title: Landscape Calculator
    Description: Computes the price of landscaping a new development based on plot width and depth, as well as grass type and tree count
"""

from DanMath import Validation

# Creates global level variables for all constant values
BASE_LABOUR = 1000
SURFACE_THRESHOLD = 5000
THRESHOLD_COST_MODIFIER = 500
TREE_COST = 100
GRASS_SQFT = ([ ["FESCUE", 0.05], 
                ["BENTGRASS", 0.02], 
                ["CAMPUS", 0.01] ])

def main():
    greeting = "| LANDSCAPING COST CALCULATOR |"

    # Outputs the greeting banner to the user
    print(("-" * len(greeting)) + "\n" + greeting + "\n" + ("-" * len(greeting)))

    # Gets user input, validates within functions
    houseNumber = getHouseNumber()
    propDimensions = [ getPropDimension(0), getPropDimension(1) ]
    print("Enter the number that corresponds to the desired grass type.")
    grassType = getGrassType()
    treeCount = getTreeCount()

    # Performs calculations
    totalCost = calculateTotalCost(propDimensions, treeCount, grassType)
    print("Total Cost for house {0}: ${1:,.2f}".format(houseNumber, totalCost))

# Gets and validates the type of grass from the user
def getGrassType():
    i = 0
    
    # Iterates through GRASS_SQFT and outputs the grass type along with its index
    # NOTE I know iterating through it is overkill to display a 3 element list but I like to keep scalability in mind if there were, say, a dozen different grass types
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
def calculateTotalCost(propDimensions, treeCount, grassType):
    # Calculates the property area
    propertyArea = int(propDimensions[0]) * int(propDimensions[1]) 

    # Calculate the total cost and, if the property area is greater than the SURFACE_THRESHOLD, add the THRESHOLD_COST_MODIFIER
    totalCost = BASE_LABOUR + (propertyArea * GRASS_SQFT[grassType][1]) + (treeCount * TREE_COST)
    if propertyArea > SURFACE_THRESHOLD:
        totalCost += THRESHOLD_COST_MODIFIER

    return totalCost

# Gets the desired number of trees from the user and validates input
def getTreeCount():
    while (treeCount := Validation.validateInt(input("Enter the number of trees desired.\n> "))) == None:
        print("Invalid input. Please enter a valid number of trees.")
    return treeCount

# NOTE I'd probably change this to a generic "validateInputInList(inputString, listToCheck)" function and add it to my Validation Class but I'm keeping it in the main file for this submission because a lot of the internal logic directly relates to rubric outcomes
# Returns converted value if inputString is in validInput list
# Returns None if inputString is not in validInput list
def validateGrassInput(inputString):
    validInput = []

    # Everything in try/except block for handling inputString if it's a string
    try:
        int(inputString)
    except:
        for i, type in enumerate(GRASS_SQFT):
            if inputString.upper() == type[0]:
                return i + 1
        return None
    
    # This point down handles inputString if it's an int
    for i in range(len(GRASS_SQFT)): # Gets the length of GRASS_SQFT and populates validInput with the indices to validate user selection
        validInput.append(str(i + 1))

    if inputString not in validInput:
        return None
    return int(inputString)

# Gets and validates property dimensions
# axis == 0 -> depth
# axis == 1 -> width
def getPropDimension(axis):
    axisString = ""
    
    if axis == 0:
        axisString = "depth"
    elif axis == 1:
        axisString = "width"

    while (propDimension := Validation.validateInt(input("Enter property {0} in feet.\n> ".format(axisString)))) == None:
        print("Invalid input. Please enter a valid {0}".format(axisString))

    while propDimension <= 0:
        while (propDimension := Validation.validateInt(input("Property {0} must be greater than 0. Please enter a valid {0}".format(axisString)))) == None:
            continue

    return propDimension

# Gets and validates house number
def getHouseNumber():
    while (houseNumber := Validation.validateInt(input("Enter Your House Number.\n> "))) == None:
        print("Invalid input. Please enter a valid house number.")
    return houseNumber

if __name__ == "__main__":
    main()