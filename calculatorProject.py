# Non GUI Calculator
# It does not follow BEDMAS currently
# vers 0.1

print('Welcome to the non-gui version of a calculator')
runProgram = True
case = 'NULL'
calculation = 0
currentValue = 0
combinedValue = ''
newCalList = list()
expressionCheck = True
finalValue = 0

def calculation(currentList):
    firstBracket = 0
    lastBracket = 0
    bracketList = [] 
    bracketValue = 0
    exponent = 0
    exponentBreak = False
    modifiedValue = 0
    valOne = 0
    valTwo  = 0
    state = 'B'
    #Use bedmas Brackets, Exponents, [Division, Multiplication,]
    #    [Addition, Subtraction]
    while(not(len(currentList) == 1)):
        for i in range(len(currentList)):
            #Check for brackets ()
            if (state == 'B'):
                if(currentList[i] == '('):
                    firstBracket = i
                    print(i)
                    print(str(i) + 'and' + str((len(currentList) - 1)))
                    #Look for the next bracket
                    for j in range(i, (len(currentList) - 1)):
                        if(currentList[j] == ')'):
                            lastBracket = j
                            print('lastB: ' + str(lastBracket))
                            if(currentList[j + 1] == '^'):
                                #Apply the exponent value to the brackets
                                exponent = int(currentList[j + 2])
                                bracketExponent(exponent, firstBracket, lastBracket) 
                                #Remove the expoent and the value
                                del currentList[currentList[j + 1] : currentList[j + 2]]
                                exponentBreak = True
                                exponent = 0 
                            break
                    #Break out of main loop to reset list(Removed two values)
                    if(exponentBreak):
                        exponentBreak = False
                        break
                    
                    #Do the calulation within the brackets
                    bracketList.insert(0, currentList[firstBracket + 1 : lastBracket])
                    print(bracketList[0])
                    bracketValue = calculation(bracketList[0])
                    print(bracketValue)
                    #Remove those values from the list
                    del currentList[firstBracket : lastBracket + 1]
                    #Add the new value, to the list
                    currentList.insert(firstBracket, bracketValue)
                    #Reset the values for future brackets
                    bracketValue = 0
                    firstBracket = 0
                    secondBracket = 0
                    #Reset the loop with the new list
                    break
                
            elif(state == 'E'):
                #Check for exponents ^
                if(currentList[i] == '^'):
                    #Apply the exponent value to the index
                    currentList[i-1] =  exponent(currentList[i + 1], currentList[i-1])
                    #Remove the exponent and it's coresponding value
                    del currentList[i : i + 1]
                    break
                
            elif(state == 'DM'):
                #Divison and Multiplication
                if(currentList[i] == '/'):
                    #Get the two surrounding values
                    valOne = int(currentList[i - 1])
                    valTwo = int(currentList[i + 1])
                    modifiedValue = valOne / valTwo
                    del currentList[i - 1 : i + 2]
                    currentList.insert(i - 1, modifiedValue)
                    modifiedValue = 0
                    break
                elif(currentList[i] == '*'):
                    #Get the two surrounding values
                    valOne = int(currentList[i - 1])
                    valTwo = int(currentList[i + 1])
                    modifiedValue = valOne * valTwo
                    del currentList[i - 1 : i + 2]
                    currentList.insert(i - 1, modifiedValue)
                    modifiedValue = 0
                    break
                
            elif(state == 'AS'):
                
                #Additon and Subtraction
                if(currentList[i] == '+'):
                    #Get the two surrounding values
                    valOne = int(currentList[i - 1])
                    valTwo = int(currentList[i + 1])
                    modifiedValue = valOne + valTwo
                    del currentList[i - 1 : i + 2]
                    currentList.insert(i - 1, modifiedValue)
                    modifiedValue = 0
                    break
                
                elif(currentList[i] == '-'):
                    #Get the two surrounding values
                    valOne = int(currentList[i - 1])
                    valTwo = int(currentList[i + 1])
                    modifiedValue = valOne - valTwo
                    del currentList[i - 1 : i + 2]
                    currentList.insert(i - 1, modifiedValue)
                    modifiedValue = 0
                    break
            
            print('Current State: ' + state + ' and index: ' + str(i))
            if(i == len(currentList) - 1):
                if(state == 'B'):
                     state = 'E'
                elif(state == 'E'):
                     state = 'DM'
                elif(state == 'DM'):
                     state = 'AS'
                else:
                     break
    print(currentList[0])
    return currentList[0]

def bracketExponent(exponent, rangeA, rangeB):
    for i in range(rangeA, rangeB):
        modifiedvalue = int(newCalList[i])
        for n in range(exponent):
            modifiedvalue *= modifiedvalue
        newCalList[i] = modifiedvalue
        
def exponent(exponentValue, value):
    modifiedvalue = value
    for i in range(exponentValue):
        modifiedvalue *= value
    return modifiedvalue
   
while(runProgram):
    print('Please input the calculation you want to solve')
    userInput = input()
    calculationList = list(userInput)
    
    #Loop through the list, and check for letters/words
    while(expressionCheck):
        while(' ' in calculationList):
            for i in range(len(calculationList)):
                if (calculationList[i] == ' '):
                    calculationList.remove(' ')
                    break
        #Ask the user to reinput the calculation, if any strings/chars were found 
        for i in range(len(calculationList)):
            try:
                int(calculationList[i])
                #Break out of the loop, when condition is met
                if(i == len(calculationList) - 1):
                    expressionCheck = False
                    break
            except ValueError:
                if(calculationList[i] == '+'):
                    """ """
                elif(calculationList[i] == '-'):
                    """ """
                elif(calculationList[i] == '*'):
                    """ """
                elif(calculationList[i] == '/'):
                    """ """
                elif(calculationList[i] == '(' or calculationList[i] == ')'):
                    """ """
                elif(calculationList[i] == '^'):
                    """ """
                else:
                    print('Please input real numbers only...')
                    print(calculationList)
                    calculationList = list()
                    userInput = input()
                    calculationList = list(userInput)
                    break
        
    
    #Combine all numbers that are not broken apart my arithmetic
    for i in range(len(calculationList)):
        #Check each of the cases for the arithmetic
        if(calculationList[i] == '+'):
            if(calculationList[i-1] == ')'):
                newCalList.insert(i, calculationList[i])
            else:
                newCalList.insert(i, combinedValue)
                newCalList.insert(i, calculationList[i])
                combinedValue = ''
            
        elif(calculationList[i] == '-'):
            if(calculationList[i-1] == ')'):
                newCalList.insert(i, calculationList[i])
            else:
                newCalList.insert(i, combinedValue)
                newCalList.insert(i, calculationList[i])
                combinedValue = ''
            
        elif(calculationList[i] == '*'):
            if(calculationList[i-1] == ')'):
                newCalList.insert(i, calculationList[i])
            else:
                newCalList.insert(i, combinedValue)
                newCalList.insert(i, calculationList[i])
                combinedValue = ''
            
        elif(calculationList[i] == '/'):
            if(calculationList[i-1] == ')'):
                newCalList.insert(i, calculationList[i])
            else:
                newCalList.insert(i, combinedValue)
                newCalList.insert(i, calculationList[i])
                combinedValue = ''

        elif(calculationList[i] == '('):
            newCalList.insert(i, calculationList[i])
                
        elif(calculationList[i] == ')'):
            if(calculationList[i-1] == ')'):
                newCalList.insert(i, calculationList[i])
            else:
                newCalList.insert(i, combinedValue)
                newCalList.insert(i, calculationList[i])
                combinedValue = ''
        else:
            combinedValue += (calculationList[i])
        #If the last index of the list, add the combined value to the list
        if(i == (len(calculationList) - 1)):
            newCalList.insert(i, combinedValue)
            break
        
    #Reactor the String list into a calculation
    finalValue = calculation(newCalList)
    runProgram = False
    
print(finalValue)
