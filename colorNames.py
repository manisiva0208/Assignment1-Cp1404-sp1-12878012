COLOR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine": "#7fffd4", "azure": "	#f0ffff",
               "beige": "#f5f5dc", "black": "#000000", "blue": "#0000ff", "brown": "#a52a2a", "burlywood": "#deb887",
               "CadetBlue": "#5f9ea0"}

color = input("Enter short state: ").lower()
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid short state")
    color = input("Enter short state: ")
