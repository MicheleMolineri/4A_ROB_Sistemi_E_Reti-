colorList = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    value = ""
    for color in colors:
        value += str(colorList.index(color))
        
    return int(value[:2])