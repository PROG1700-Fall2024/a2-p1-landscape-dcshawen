"""
    Author: Dan Shaw w0190983
    Title: Landscape Calculator
    Description: Computes the price of landscaping a new development based on plot address, width and length
"""

# Creates global level variables for all constant values
BASE_LABOUR = 1000
SURFACE_THRESHOLD = 5000
THRESHOLD_COST_MODIFIER = 500
TREE_COST = 100
GRASS_SQFT = ([ ["FESCUE", 0.05], ["BENTGRASS", 0.02], ["CAMPUS", 0.01] ])

propDimensions = []

def main():
    global propDimensions
    # Declare some local variables
    greeting = "| Landscaping Cost Calculator |"

    # Output greeting banner to user
    print("-" * len(greeting))
    print(greeting)
    print("-" * len(greeting))

    houseNumber = getHouseNumber()
    propDimensions = [ getPropDimension(0), getPropDimension(1) ]

    grassType = getGrassType()
    # Get number of trees from the user
    treeCount = int(getTreeCount())
    totalCost = calculateValues(treeCount, grassType)
    print(totalCost)


def getGrassType():
    global GRASS_SQFT
    i = 0
    print("Enter the number that corresponds to the desired grass type.")
    
    for row in GRASS_SQFT:
        print("\t({0}) {1}".format(i + 1, row[0]))
        i += 1
    
    #TODO VALIDATE
    index = int(input("> "))
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

def getTreeCount():
    return input("Enter the number of trees desired.\n> ")

# Attempt to convert grassInput to an int, if it's successful check that it falls within the expected range for grass type indices
# Return converted value if successful
# Should return None if fails
def validateGrassInput(inputString):
    return True
    
def getPropDimension(i):
    if i == 0:
        return input("Enter property depth in feet.\n> ")
    elif i == 1:
        return input("Enter property width in feet.\n> ")
    else:
        print("Invalid use of getPropDimensions()")

def getHouseNumber():
    return input("Enter Your House Number.\n> ")

if __name__ == "__main__":
    main()