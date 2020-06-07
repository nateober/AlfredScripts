import sys, json, subprocess, re


def wordCount(query):
    theList = re.split('[\W]+', query)  
    theList = list(filter(None, theList))
    return len(theList)

def wordList(query):
    theList = re.split('[\W]+', query)  
    theList = list(filter(None, theList))
    return theList

def charCount(query):
	return len(query)

args = subprocess.check_output("pbpaste", universal_newlines=True)

wc = wordCount(args)
cc = charCount(args)
wl = wordList(args)

wcString = "Number of words: {}".format(wc)
ccString = "Number of characters = {}".format(cc)
wordList = "{}...".format(wl[0:10])

result = {"items": [
    {
        "uid": "words",
        "title": "Words",
        "subtitle": wcString,
        "arg": wc,
    },
	{
        "uid": "words",
        "title": "Chars",
        "subtitle": ccString,
        "arg": cc,
    },
    {
        "uid": "words",
        "title": "Word List",
        "subtitle": wordList,
        "arg": json.dumps(wl),
    }
]}

finalResult = json.dumps(result)
print(finalResult)