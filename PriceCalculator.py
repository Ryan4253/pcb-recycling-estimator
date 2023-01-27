ALUMINUM_CONTENT = {
    "Capacitor"   : 0.35,
    "IC"          : 0,
    "MLCC"        : 0,
    "Heatsink_Al" : 0.9,
    "Heatsink_Cu" : 0,
    "RJ45"        : 2.2,
    "USB"         : 0,
    "DB9"         : 0.2,
    "HDMI"        : 1.6
}

COPPER_CONTENT = {
    "Capacitor"   : 0,
    "IC"          : 0.000016,
    "MLCC"        : 0.38,
    "Heatsink_Al" : 0,
    "Heatsink_Cu" : 5.5,
    "RJ45"        : 0,
    "USB"         : 0.6,
    "DB9"         : 0.5,
    "HDMI"        : 0
}

GOLD_CONTENT = {
    "Capacitor"   : 0,
    "IC"          : 0.000017,
    "MLCC"        : 0,
    "Heatsink_Al" : 0,
    "Heatsink_Cu" : 0,
    "RJ45"        : 0,
    "USB"         : 0,
    "DB9"         : 0,
    "HDMI"        : 0
}

IRON_CONTENT = {
    "Capacitor"   : 0,
    "IC"          : 0,
    "MLCC"        : 0,
    "Heatsink_Al" : 0,
    "Heatsink_Cu" : 0,
    "RJ45"        : 0,
    "USB"         : 1.5,
    "DB9"         : 4.3,
    "HDMI"        : 0
}

METAL_PRICE = {
    "Aluminum" : 0.021,
    "Copper"   : 0.090,
    "Gold"     : 1939.417,
    "Iron"     : 0.294
}

def calculatePrice(detectionResult : dict):
    price = 0
    for category, number in detectionResult.items():
        unitPrice = (ALUMINUM_CONTENT[category] * METAL_PRICE["Aluminum"] + 
                     COPPER_CONTENT[category]   * METAL_PRICE["Copper"] + 
                     GOLD_CONTENT[category]     * METAL_PRICE["Gold"] + 
                     IRON_CONTENT[category]     * METAL_PRICE["Iron"])
        price += number * unitPrice

    return price
