import sys, json, subprocess, numpy, re


def splitInput(query):
    theList = re.split(r'\D+', query)  
    theList = list(filter(None, theList))
    return theList

def sumList(inList):
    outNumber = 0
    for num in inList:
        outNumber += num
    return outNumber

def avgList(inList):
	outNumber = 0
	count = len(inList)
	for num in inList:
		outNumber += num
	return outNumber/count

def stdDeviation(inList):
	return numpy.std(numpy.array(inList).astype(numpy.float))

args = subprocess.check_output("pbpaste", universal_newlines=True)

outSum = sumList(splitInput(args))
outAvg = avgList(splitInput(args))
outDev = stdDeviation(splitInput(args))

sumString = "The sum = {}".format(outSum)
avgString = "The average = {}".format(outAvg)
devString = "The average = {}".format(outDev)

result = {"items": [
    {
        "uid": "maths",
        "title": "Sum",
        "subtitle": sumString,
        "arg": outSum,
    },
	{
        "uid": "maths",
        "title": "Average",
        "subtitle": avgString,
        "arg": outAvg,
    },
	{
        "uid": "maths",
        "title": "Standard Deviation",
        "subtitle": devString,
        "arg": outDev,
    },
    {
        "uid": "maths",
        "title": "distribution",
        "subtitle": json.dumps(splitInput(args)),
        "arg": json.dumps(splitInput(args)),
    }
]}

finalResult = json.dumps(result)
print(finalResult)