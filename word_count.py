
#Read the stop words file
with open('./stopwords.txt') as f:
    lines = f.readlines()
    lines[:] = [line.rstrip('\n') for line in lines]
    #print (lines)


#Index function - used to create unique word and respective count pairs.
def index(string, name1, finalDict):
    myString = string
    myDict = {}
    for item in myString:
        if item in myDict:
            myDict[item] += 1
        else:
            myDict[item] = 1
    
    for item in myDict:
        temp = (name1, myDict[item])
        if item in finalDict:
            temp_list = finalDict[item]
            temp_list.append(temp)
        else:
            finalDict[item] = [temp]

#Search function used to search for a query and  give the desired output
def search(stringCheck, finalDict, docID):
    strings = stringCheck.replace("(","")
    strings = strings.replace(")","")
    strings = strings.split()
    count = 0
    finalRes = {}
    for stringName in strings:
        print (stringName)
        strName = stringName.lower()
        if strName in finalDict:
            result = finalDict[strName]
        else:
            result = []
        tempResult = {}
        midRes = {}
        for i in range(0, len(result)):
            tempResult[result[i][0]] = result[i][1]
        
        for item in docID:
            if item in tempResult:
                midRes[item] = tempResult[item]
            else:
                midRes[item] = 0
        for key in sorted(midRes):
            print ("Doc : ",key,"  Freq : ", midRes[key])
        if count == 0:
            finalRes = midRes
        else:
            for item in docID:
                finalRes[item] += midRes[item]
        count = 1
        print ("\n")
    if len(strings) != 1:
        print (stringCheck)
    finalResult = {}
    
    for key in finalRes:
        if len(strings) != 1:
            print ("Doc : ",key,"  Freq : ", finalRes[key])
        if finalRes[key] != 0:
            finalResult[key] = finalRes[key]
    print ("\n")
    if (finalResult):
        sorted_map = sorted(finalResult.items(), key=op.itemgetter(1))
        print (sorted_map[::-1])
    else:
        print ('No results found!')
           

import glob
import operator as op

path = './Random_files/*.txt'
files = glob.glob(path)

finalDict = {}
docID = []
for name in files:
    docID.extend([name[-6: -4]])
    with open(name) as f:
        for line in f:
            lines1=line.lower()
            lines1 = lines1.replace("(","")
            lines1 = lines1.replace(")","")
            word=lines1.split()

            stop=[c for c in word if c not in lines]   

            index(stop,name[-6: -4],finalDict)


stringCheck = str(input('Enter String: '))


search(stringCheck, finalDict, docID)