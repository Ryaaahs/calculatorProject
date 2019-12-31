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

while(runProgram):
    print('Please input the calculation you want to solve')
    userInput = input()
    calculationList = list(userInput)
    
    #Loop through the list, and check for letters/words
    while(expressionCheck):
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
       
        
            
    #Reactor the String list into a calculation
    for i in range(len(newCalList)):
        try:
            #Check the current arithmitic options
            if(case == 'ADD'):
                currentValue += int(newCalList[i])
                case = 'NULL'
            elif(case == 'SUB'):
                currentValue -= int(newCalList[i])
                case = 'NULL'
            elif(case == 'MULTI'):
                currentValue *= int(newCalList[i])
                case = 'NULL'
            elif(case == 'DIV'):
                currentValue /= int(newCalList[i])
                case = 'NULL'
            else:
                currentValue = int(newCalList[i])
        except TypeError:
            print('This is a string u douche')
        except ValueError:
            #Apply them 
            if(newCalList[i] == '+'):
                case = 'ADD'
                
            elif(newCalList[i] == '-'):
                case = 'SUB'
            
            elif(newCalList[i] == '*'):
                case = 'MULTI' 
            
            elif(newCalList[i] == '/'):
                case = 'DIV'
                
    runProgram = False
print(currentValue)
