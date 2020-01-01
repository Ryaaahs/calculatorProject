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

def calculate(list):
    while(not(len(list) == 1)):
        for i in range(len(list)):
            #Divison and Multiplication
                if(bracketList[i] == '/'):
                    #Get the two surrounding values
                    valOne = int(bracketList[i - 1])
                    valTwo = int(bracketList[i + 1])
                    modifiedValue = valOne / valTwo
                    del bracketList[i - 1 : i + 1]
                    bracketList[i - 1] = modifiedValue
                    modifiedValue = 0
                    break
                elif(bracketList[i] == '*'):
                    #Get the two surrounding values
                    valOne = int(bracketList[i - 1])
                    valTwo = int(bracketList[i + 1])
                    modifiedValue = valOne * valTwo
                    del bracketList[i - 1 : i + 1]
                    bracketList[i - 1] = modifiedValue
                    modifiedValue = 0
                    break

                #Additon and Subtraction
                if(bracketList[i] == '/'):
                    #Get the two surrounding values
                    valOne = int(bracketList[i - 1])
                    valTwo = int(bracketList[i + 1])
                    modifiedValue = valOne / valTwo
                    del bracketList[i - 1 : i + 1]
                    bracketList[i - 1] = modifiedValue
                    modifiedValue = 0
                    break
                elif(bracketList[i] == '*'):
                    #Get the two surrounding values
                    valOne = int(bracketList[i - 1])
                    valTwo = int(bracketList[i + 1])
                    modifiedValue = valOne * valTwo
                    del bracketList[i - 1 : i + 1]
                    bracketList[i - 1] = modifiedValue
                    modifiedValue = 0
                    break
    return list[0]

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
        #(1 + 1) + 4 + 4
        while(True):
            #Break apart the brackets
            for i in range(len(calculationList)):
                print(len(calculationList[i])
                if ('(' or ')' in calculationList[i] and len(calculationList[i]) > 1):
                    print(calculationList)
                    bracketList = list(calculationList[i])
                    calculationList.insert(i + 1, bracketList)
                    calculationList.insert(i + 2, bracketList)
                    del calculationList[i]  
            #Check to see if all brackets are broken apart
            #for i in range(len(calculationList)):
                #if
        #Delete all the blank strings within the list
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
            newCalList.insert(i, combinedValue)
            newCalList.insert(i, calculationList[i])
            combinedValue = ''
            
        elif(calculationList[i] == '-'):
            newCalList.insert(i, combinedValue)
            newCalList.insert(i, calculationList[i])
            combinedValue = ''
            
        elif(calculationList[i] == '*'):
            newCalList.insert(i, combinedValue)
            newCalList.insert(i, calculationList[i])
            combinedValue = ''
            
        elif(calculationList[i] == '/'):
            newCalList.insert(i, combinedValue)
            newCalList.insert(i, calculationList[i])
            combinedValue = ''
            
        else:
            combinedValue += (calculationList[i])

        #If the last index of the list, add the combined value to the list
        if(i == (len(calculationList) - 1)):
            newCalList.insert(i, combinedValue)
            break
       
        
    #Use bedmas Brackets, Exponents, [Division, Multiplication,]
    #    [Addition, Subtraction]
    
    #Reactor the String list into a calculation
    while(not(len(newCalList) == 1)):
        for i in range(len(newCalList)):
            #Check for brackets ()
            if (state == 'B'):
                if(newCalList[i] == '('):
                    firstBracket = newCalList[i]
                    #Look for the next bracket
                    for j in range(i, (len(newCalList) - 1)):
                        if(newCalList[j] == ')'):
                            secondBracket = newCalList[j]
                            if(newCalList[j + 1] == '^'):
                                #Apply the exponent value to the brackets
                                exponent = int(newCalList[j + 2])
                                bracketExponent(exponent, firstBracket, secondBracket) 
                                #Remove the expoent and the value
                                del newCalList[newCalList[j + 1] : newCalList[j + 2]]
                                exponentBreak = True
                                exponent = 0 
                            break
                    #Break out of main loop to reset list(Removed two values)
                    if(exponentBreak):
                        exponentBreak = False
                        break
                    #Do the calulation within the brackets
                    bracketList = newCalList[firstBracket : secondBracket]
                    bracketValue = calculate(bracketList)
                    #Remove those values from the list
                    del newCalList[firstBracket : secondBracket]
                    #Add the new value, to the list
                    newCalList.insert(firstBracket, bracketValue)
                    #Reset the values for future brackets
                    bracketValue = 0
                    firstBracket = 0
                    secondBracket = 0
                    #Reset the loop with the new list
                    break
            elif(state == 'E'):
                #Check for exponents ^
                if(newCalList[i] == '^'):
                    #Apply the exponent value to the index
                    newCalList[i-1] =  exponent(newCalList[i + 1], newCalList[i-1])
                    #Remove the exponent and it's coresponding value
                    del newCalList[i : i + 1]
                    break
            elif(state == 'DM'):
                #Divison and Multiplication
                if(newCalList[i] == '/'):
                    #Get the two surrounding values
                    valOne = int(newCalList[i - 1])
                    valTwo = int(newCalList[i + 1])
                    modifiedValue = valOne / valTwo
                    del newCalList[i - 1 : i + 2]
                    newCalList.insert(i - 1, modifiedValue)
                    modifiedValue = 0
                    break
                elif(newCalList[i] == '*'):
                    #Get the two surrounding values
                    valOne = int(newCalList[i - 1])
                    valTwo = int(newCalList[i + 1])
                    modifiedValue = valOne * valTwo
                    del newCalList[i - 1 : i + 2]
                    newCalList.insert(i - 1, modifiedValue)
                    modifiedValue = 0
                    break
                
            elif(state == 'AS'):
                
                #Additon and Subtraction
                if(newCalList[i] == '+'):
                    #Get the two surrounding values
                    valOne = int(newCalList[i - 1])
                    valTwo = int(newCalList[i + 1])
                    modifiedValue = valOne + valTwo
                    del newCalList[i - 1 : i + 2]
                    newCalList.insert(i - 1, modifiedValue)
                    modifiedValue = 0
                    break
                
                elif(newCalList[i] == '-'):
                    #Get the two surrounding values
                    valOne = int(newCalList[i - 1])
                    valTwo = int(newCalList[i + 1])
                    modifiedValue = valOne - valTwo
                    del newCalList[i - 1 : i + 2]
                    newCalList.insert(i - 1, modifiedValue)
                    modifiedValue = 0
                    break
            
            print(newCalList)
            print('Current State: ' + state + ' and index: ' + str(i))
            if(i == len(newCalList) - 1):
                if(state == 'B'):
                    state = 'E'
                elif(state == 'E'):
                    state = 'DM'
                elif(state == 'DM'):
                    state = 'AS'
                else:
                    break
    runProgram = False
print(newCalList[0])
