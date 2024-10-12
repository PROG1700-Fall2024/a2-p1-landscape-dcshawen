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

#NOTE I wish multidimensional arrays didn't behave so weird in Python because they'd be a better choice than a dictionary
GRASS_SQFT = {
    "FESCUE": 0.05,
    "BENTGRASS": 0.02,
    "CAMPUS": 0.01
}
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
    # Output selected grass type
    print("You have selected {0} grass.".format(grassType.capitalize()))

    # Get number of trees from the user
    treeCount = int(getTreeCount())

    print("The total cost for landscaping property {0} is ${1:,.2f}".format(houseNumber, calculateValues(treeCount, grassType)))

def getGrassType():
    global GRASS_SQFT
    i = 0
    print("Enter the number that corresponds to the desired grass type.")

    # Iterates through dictionary items and outputs them to the user
    #NOTE Iterating through it is why a multidimensional array would have been better but the dataset is small enough I'm not worried about it
    for key, value in GRASS_SQFT.items():
        i += 1
        print("\t({0}) {1}".format(i, key.capitalize()))
    
    #TODO VALIDATE
    index = input("> ")
    grassType = getGrassTypeFromIndex(index)

    return grassType

def calculateValues(treeCount, grassType):
    # Get access to global variables
    global BASE_LABOUR, SURFACE_THRESHOLD, THRESHOLD_COST_MODIFIER, TREE_COST, GRASS_SQFT, propDimensions

    propertyArea = int(propDimensions[0]) * int(propDimensions[1]) 
    if propertyArea > SURFACE_THRESHOLD:
        totalCost = BASE_LABOUR + (treeCount * TREE_COST) + (propertyArea * GRASS_SQFT[grassType]) + THRESHOLD_COST_MODIFIER
    else:
        totalCost = BASE_LABOUR + (propertyArea * GRASS_SQFT[grassType]) + (treeCount * TREE_COST)

    return totalCost

def getGrassTypeFromIndex(index):
    match index:
        case "1":
            return "FESCUE"
        case "2":
            return "BENTGRASS"
        case "3":
            return "CAMPUS"
        case _:
            return None

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