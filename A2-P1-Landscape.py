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

propDimensions = []

def main():
    global propDimensions
    # Declare some local variables
    greeting = "| Landscaping Cost Calculator |"

    # Output greeting banner to user
    print("-" * len(greeting))
    print(greeting)
    print("-" * len(greeting))

    # Get user input, validate within functions
    houseNumber = getHouseNumber()
    propDimensions = [ getPropDimension(0), getPropDimension(1) ]
    grassType = getGrassType()
    treeCount = getTreeCount()

    # Perform calculations
    totalCost = calculateValues(treeCount, grassType)
    print(totalCost)


def getGrassType():
    global GRASS_SQFT
    i = 0
    print("Enter the number that corresponds to the desired grass type.")
    
    for row in GRASS_SQFT:
        print("\t({0}) {1}".format(i + 1, row[0])) # Add 1 to account for 0-indexing
        i += 1
    
    while (index := validateGrassInput(input("> "))) is None:
        print("Invalid input. Please enter a valid grass type.")
    
    # Subtract 1 to get back to 0-indexing
    index -= 1

    # Output selected grass type
    print("You have selected {0} grass.".format(GRASS_SQFT[index][0].capitalize()))
    return index

def calculateValues(treeCount, grassType):
    # Get access to global variables
    global BASE_LABOUR, SURFACE_THRESHOLD, THRESHOLD_COST_MODIFIER, TREE_COST, GRASS_SQFT, propDimensions

    propertyArea = int(propDimensions[0]) * int(propDimensions[1]) 
    if propertyArea > SURFACE_THRESHOLD:
        totalCost = BASE_LABOUR + (treeCount * TREE_COST) + (propertyArea * GRASS_SQFT[grassType][1]) + THRESHOLD_COST_MODIFIER
    else:
        totalCost = BASE_LABOUR + (propertyArea * GRASS_SQFT[grassType][1]) + (treeCount * TREE_COST)

    return totalCost

# Attempt to convert value to int. If successful return the converted value
# If fails, return None
def validateInt(value):
    try:
        return int(value)
    except:
        return None

def getTreeCount():
    while (treeCount := validateInt(input("Enter the number of trees desired.\n> "))) is None:
        print("Invalid input. Please enter a valid number of trees.")
    return treeCount

# Return converted value if inputString is in validInput list
# Return None if inputString is not in validInput list
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

def getPropDimension(i):
    if i == 0:
        while (propDimension := validateInt(input("Enter property depth in feet.\n> "))) is None:
            print("Invalid input. Please enter a valid property depth.")
        return propDimension
    elif i == 1:
        while (propDimension := validateInt(input("Enter property width in feet.\n> "))) is None:
            print("Invalid input. Please enter a valid property width.")
        return propDimension

def getHouseNumber():
    while (houseNumber := validateInt(input("Enter Your House Number.\n> "))) is None:
        print("Invalid input. Please enter a valid house number.")
    return houseNumber

if __name__ == "__main__":
    main()