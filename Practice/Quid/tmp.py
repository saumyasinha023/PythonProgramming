from collections import defaultdict


def calculateScore(text,prefix,suffix):
    input_len=len(text)
    suffixLen=len(suffix)
    prefixLen=len(prefix)
    tmp = -1
    # create a dictionary to store the count of occurences of every string
    counter=defaultdict(int)
    # set() to store every substring of tex, suffix and prefix
    keys=set()

    for i in range(input_len):
        for j in range(i+1, input_len + 1):
            tmpText=text[i:j]
            preString=0
            subString=0
            subLen=len(tmpText)
            # creating substrings from text and suffix
            for each in range(len(tmpText)):
                if(subLen-each<=suffixLen):
                    if(tmpText[each:]==suffix[0:subLen-each]):
                        preString=max(subLen-each,preString)
            # creating substrings from text and prefix
            for each in range(subLen):
                if prefixLen>each:
                    if(prefix[prefixLen-each-1:prefixLen]==tmpText[0:each+1]):
                        subString=max(each,subString)
                counter[tmpText]=max(counter[tmpText],subString+preString)
    # adding each substring to set()
    for each in counter:
        keys.add(each)
    keyArr=sorted(keys)
    finalString=None
    for each_val in (keyArr):
        if counter[each_val]>tmp:
            finalString=each_val
            tmp=counter[each_val]
    return finalString
