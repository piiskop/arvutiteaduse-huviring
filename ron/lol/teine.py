print("Auh!")
name = input("Mis on su nimi? ")
print("Kas su nimi on tõesti " + name + "?")
if len(name) > 7:
    print("Sul on pikk nimi.")
else:
    print("Sul on lühike nimi.")
def askForName():
    print("Auh!")
name = input("Mis on su nimi? ")
print("Kas su nimi on tõesti " + name + "?")
if len(name) > 7:
    print("Sul on pikk nimi.")
else:
    print("Sul on lühike nimi.")
askForName()
def countCharacter(string, character):
    numberOfOccurencies = 0
    lengthOfString= len(string)
    index = 0
    while index < lengthOfString:
        if string[index] == character:
            numberOfOccurencies += 1
        index += 1
    return numberOfOccurencies
numberOfOccurencies = countCharacter(name, "t")
sentence = "Sinu nimes esineb t-täht {0} korral."
print(sentence.format(numberOfOccurencies))
