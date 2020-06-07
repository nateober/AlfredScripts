import sys, re, uuid, time, urllib, subprocess
def splitInput(query):
    linesList = query.splitlines()
    commaList = query.split(",")
    spaceList = query.split()

    if len(linesList) > 1:
        theList = linesList
    elif len(commaList) > 1:
        theList = commaList
    elif len(spaceList) > 1:
        theList = spaceList  
    
    return theList

def mapTrim(str):
    return str.strip()

def mapIndent(str):
    return(re.sub("^", "\t", str))

def mapUnindent(str):
    return(re.sub("^\t", "", str))

def numberList(inList):
    for num, word in enumerate(inList):
        print("{}. {}".format(num+1, word.strip()))

def removeNumberList(inList):
    for num, word in enumerate(inList):
        print(re.sub("^\d+.(\.)? ", "", word))

def sumList(inList):
    outNumber = 0
    for num in inList:
        if num != "":
            outNumber += int(num)
    
    print(outNumber)

def avgList(inList):
    outNumber = 0
    count = len(inList)
    for num in inList:
        if num != "":
            outNumber += int(num)

    print(round(outNumber/count, 2))

def sortList(inList):
    inList.sort()
    for line in inList:
       print("{}".format(line)) 

def reverseSortList(inList):
    inList.sort(reverse = True)
    for line in inList:
       print("{}".format(line)) 

def sortUnique(inList):
    trimList = map(mapTrim, inList)
    uniqueList = list(set(trimList)) 
    uniqueList.sort()
    for line in uniqueList:
       print("{}".format(line)) 

def commaSeparate(inList):
    output = filter(bool, map(mapTrim, inList))
    print(", ".join(output))

def inSqlQuoted(inList):
    readyList = filter(bool, map(mapTrim, inList))
    connected = "\', \'".join(readyList)
    myFormat = "(\'{}\')"
    print(myFormat.format(connected))

def inSql(inList):
    readyList = filter(bool, map(mapTrim, inList))
    connected = ", ".join(readyList)
    myFormat = "({})"
    print(myFormat.format(connected))

def grepOr(inList):
    readyList = filter(bool, map(mapTrim, inList))
    connected = "\'\\|\'".join(readyList)
    myFormat = "\'{}\'"
    print(myFormat.format(connected))

def toArray(inList):
    readyList = filter(bool, map(mapTrim, inList))
    connected = "\", \"".join(readyList)
    myFormat = "[\"{}\"]"
    print(myFormat.format(connected))

def toLower(theQuery):
    print(theQuery.lower())

def toCapital(theQuery):
    print(theQuery.upper())

def toTitle(theQuery):
    print(theQuery.title())

def reverseSlashes(theQuery):
    out = re.sub("\\\\", "/", theQuery)
    print(out)

def characterCount(theQuery):
    print(len(theQuery))

def guid():
    print(uuid.uuid1())

def ms():
    millis = int(round(time.time() * 1000))
    print(millis)

def indent(inList):
    output = map(mapIndent, inList)
    for line in output:
       print("{}".format(line)) 

def unindent(inList):
    output = map(mapUnindent, inList)
    for line in output:
       print("{}".format(line)) 

def urlencode(str):
    print(urllib.quote(str))

def urldecode(str):
   print(urllib.unquote(str))


#query = sys.argv[1]

def run(query):
    clipboard = subprocess.check_output("pbpaste", universal_newlines=True)

    if query == "nl":
        numberList(splitInput(clipboard))
    elif query == "rn":
        removeNumberList(splitInput(clipboard))
    elif query == "sort":
        sortList(splitInput(clipboard))
    elif query == "rsort":
        reverseSortList(splitInput(clipboard))
    elif query == "usort":
        sortUnique(splitInput(clipboard))
    elif query == "sum":
        sumList(splitInput(clipboard))
    elif query == "avg":
        avgList(splitInput(clipboard))
    elif query == "array":
        toArray(splitInput(clipboard))
    elif query == "sqlIn":
        inSql(splitInput(clipboard))
    elif query == "sqlInQuoted":
        inSqlQuoted(splitInput(clipboard))
    elif query == "grepOr":
        grepOr(splitInput(clipboard))
    elif query == "comma":
        commaSeparate(splitInput(clipboard))
    elif query == "indent":
        indent(splitInput(clipboard))
    elif query == "unindent":
        unindent(splitInput(clipboard))
    elif query == "slashes":
        reverseSlashes(clipboard)
    elif query == "urlEncode":
        urlencode(clipboard)
    elif query == "urlUnencode":
        urldecode(clipboard)
    elif query == "toLower":
        toLower(clipboard)
    elif query == "toCaps":
        toCapital((clipboard))
    elif query == "cc":
        characterCount((clipboard))
    elif query == "guid":
        guid()
    elif query == "ms":
        ms()
 




