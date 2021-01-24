import sys

# Tenga en cuenta las variables y arreglos que se esten creando en c++

x = open("input.txt", "r")

# Checar si el codigo es valido
codeValid = False

for line in x:
    if "main()" in line:
        codeValid = True
        break
if not codeValid:
    print("Invalid Input!")

# Buscar las primeras variables

intVals = {}
intValsName = []

for secondLine in x:

    # Declaracion de variable

    intFound = secondLine.find('int')
    if intFound != -1:

        currentIndex = intFound + 4

        while True:

            newVariable = ""
            equalFound = False
            equalIndex = -1

            for i in range(currentIndex, len(secondLine)):
                currentIndex = i
                if secondLine[i] == '=':
                    equalFound = True
                    equalIndex = i
                    break
                elif secondLine[i] == ',' or secondLine[i] == ';':
                    break
                newVariable += secondLine[i]

            while newVariable[0] == ' ':
                newVariable = newVariable[1:]

            while newVariable[-1] == ' ':
                newVariable = newVariable[:len(newVariable) - 1]

            value = 'null'

            if equalFound:
                strValue = ""
                for i in range(equalIndex + 1, len(secondLine)):
                    currentIndex += 1
                    if secondLine[i] == ',' or secondLine[i] == ';':
                        break
                    strValue += secondLine[i]

                value = int(strValue)

            intVals[newVariable] = value
            intValsName.append(newVariable)
            if secondLine[currentIndex] == ';':
                break
            else:
                currentIndex += 1

    # Update Variable

    for elem in intValsName:
        variableIndex = secondLine.find(' ' + elem + ' ')
        if variableIndex != -1:
            variableIndex += len(elem)

            valid = False
            newValue = ""
            for i in range(variableIndex, len(secondLine)):
                if secondLine[i] == '=' and secondLine[variableIndex + 1] != '=':  # Valida
                    valid = True
                elif valid:
                    if secondLine[i] == ';':
                        break
                    newValue += secondLine[i]

            while newValue[0] == ' ':
                newValue = newValue[1:]

            while newValue[-1] == ' ':
                newValue = newValue[:len(newValue) - 1]

            intVals[elem] = newValue

# print(intValsName)
print(intVals)
