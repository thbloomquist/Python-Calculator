numFormula = input("Enter your formula")
listFormula = list(numFormula)

#add logic to group numbers together
def checkForSpaces(thisList):
    spaceCount = 0
    for i in range (0, len(thisList)-1):
        if(thisList[i] == ' '):
            spaceCount = spaceCount+1
    while(spaceCount != 0):
        thisList.remove(' ')
        spaceCount = spaceCount-1

def combineNumbers(thisList):
    tempStartIndex = len(thisList)+1
    tempEndIndex = len(thisList)+1
    for i in range (0, len(thisList)-1):
        tempNumber = len(thisList)
        if(i == tempNumber):
            return
        if((thisList[i] != '+') & (thisList[i] != '*') & (thisList[i] != '/') & (thisList[i] != '-') & (thisList[i] != '(') & (thisList[i] != ')') & (thisList[i] != '^')):
            tempStartIndex = i
            tempEndIndex = tempStartIndex
            going = True
            while(going):
                if(tempEndIndex != len(thisList)-1):
                    tempEndIndex = tempEndIndex + 1
                else:
                    going = False
                if((thisList[tempEndIndex] == '+') | (thisList[tempEndIndex] == '*') | (thisList[tempEndIndex] == '/') | (thisList[tempEndIndex] == '-') | (thisList[tempEndIndex] == '(') | (thisList[tempEndIndex] == ')') | (thisList[tempEndIndex] == '^')):
                    going = False
            if(tempStartIndex != tempEndIndex):
                oneNumber = thisList.copy()
                if(tempEndIndex == len(thisList)-1):
                    oneNumber = oneNumber[tempStartIndex:tempEndIndex+1]
                    stringThing = ''.join(oneNumber)
                    if(stringThing[-1] == ')'):
                        stringThing = stringThing[:-1]
                        del thisList[tempStartIndex:tempEndIndex]
                        thisList.insert(tempStartIndex, stringThing)
                    else:
                        del thisList[tempStartIndex:tempEndIndex+1]
                        thisList.insert(tempStartIndex, stringThing)

                else:
                    oneNumber = oneNumber[tempStartIndex:tempEndIndex]
                    stringThing = ''.join(oneNumber)
                    del thisList[tempStartIndex:tempEndIndex]
                    thisList.insert(tempStartIndex, stringThing)

def parenthesesError(thisList):
    num = thisList.count(')')
    num2 = thisList.count('(')
    if(num != num2):
        return True
    else:
        return False

def containsParentheses(thisList):
    num = thisList.count(')')
    num2 = thisList.count('(')
    if((num > 0) | (num2 > 0)):
        return True
    else:
        return False
    
def findInwardParenthese(thisList):
    tempIndex = 0
    tempNum = len(thisList)-1
    while(tempNum != 0):
        if(thisList[tempNum] == ')'):
            tempIndex = tempNum
        tempNum = tempNum - 1
    return tempIndex

def completeParenthese(thisList, indexOf):
    tempIndex = 0
    while(indexOf >= 0):
        if(thisList[indexOf] == '('):
            tempIndex = indexOf
            return tempIndex
        indexOf = indexOf - 1

def calculator(thisList):
    #handle exponents first
    if(thisList.count('^') != 0):
        countOfExps = thisList.count('^')
        while(countOfExps != 0):
            firstExp = thisList.index('^')
            calcExp = float(thisList[firstExp-1]) ** float(thisList[firstExp+1])
            thisList[firstExp] = calcExp
            thisList.pop(firstExp-1)
            thisList.pop(firstExp)
            countOfExps = countOfExps-1
    #logic must be added to figure out if division sign comes before mult or vice versa
    multCount = thisList.count('*')
    divCount = thisList.count('/')
    if((divCount != 0) | (multCount != 0)):
        while((multCount != 0) | (divCount != 0)):
            multIndex = len(thisList)+1
            divIndex = len(thisList)+1
            if(multCount != 0):
                multIndex = thisList.index('*')
            if(divCount != 0):
                divIndex = thisList.index('/')
            if((multIndex < divIndex)):
            #this means multiplication happens first
                calcMult = float(thisList[multIndex-1]) * float(thisList[multIndex+1])
                thisList[multIndex] = calcMult
                thisList.pop(multIndex-1)
                thisList.pop(multIndex)
                multCount = multCount - 1
            elif((divIndex < multIndex)):
                calcDiv = float(thisList[divIndex-1]) / float(thisList[divIndex+1])
                thisList[divIndex] = calcDiv
                thisList.pop(divIndex-1)
                thisList.pop(divIndex)
                divCount = divCount - 1
    addCount = thisList.count('+')
    subCount = thisList.count('-')
    if((addCount != 0) | (subCount != 0)):
        while((addCount != 0) | (subCount != 0)):
            addIndex = len(thisList)+1
            subIndex = len(thisList)+1
            if(addCount != 0):
                addIndex = thisList.index('+')
            if(subCount != 0):
                subIndex = thisList.index('-')
            if((addIndex < subIndex)):
                calcAdd = float(thisList[addIndex-1]) + float(thisList[addIndex+1])
                thisList[addIndex] = calcAdd
                thisList.pop(addIndex-1)
                thisList.pop(addIndex)
                addCount = addCount - 1
            elif((subIndex < addIndex)):
                calcSub = float(thisList[subIndex-1]) - float(thisList[subIndex+1])
                thisList[subIndex] = calcSub
                thisList.pop(subIndex-1)
                thisList.pop(subIndex)
                subCount = subCount - 1
    #logic must be added to figure out if addition sign comes before sub or vice versa

checkForSpaces(listFormula)
combineNumbers(listFormula)

if(containsParentheses(listFormula)):
    if(parenthesesError(listFormula)):
        print("Parentheses Error")
        exit()
    else:
        parenCount = listFormula.count(')')
        while(parenCount != 0):
            firstParenthese = findInwardParenthese(listFormula)
            #print("Inward Parenthese at index" , firstParenthese)
            secondParenthese = completeParenthese(listFormula, firstParenthese)
            #print("Outward Parenthese at index ", secondParenthese)
            subList = listFormula.copy()
            subList = subList[secondParenthese:firstParenthese+1]
            #print("subList =", subList)
            subList.pop(len(subList)-1)
            subList.pop(0)
            #print("subList2 = ", subList)
            calculator(subList)
            del listFormula[secondParenthese:firstParenthese+1]
            if(subList != None):
                listFormula.insert(secondParenthese, float(subList[0]))
            #print("List Formula is now", listFormula)
            parenCount = parenCount - 1
#previous statements handle all logic within parentheses
#if there is math not in parentheses need to do one more once over

calculator(listFormula)

print("Your calculated value =", listFormula[0])

