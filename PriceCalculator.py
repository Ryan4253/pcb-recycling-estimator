import Constants

def calculatePrice(detectionResult : dict):
    price = 0
    for category, number in detectionResult.items():
        unitPrice = (Constants.ALUMINUM_CONTENT[category] * Constants.METAL_PRICE["Aluminum"] + 
                     Constants.COPPER_CONTENT[category]   * Constants.METAL_PRICE["Copper"] + 
                     Constants.GOLD_CONTENT[category]     * Constants.METAL_PRICE["Gold"] + 
                     Constants.IRON_CONTENT[category]     * Constants.METAL_PRICE["Iron"])
        price += number * unitPrice

    return price
