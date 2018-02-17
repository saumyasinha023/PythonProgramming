def validIPAddress(IP):
    finalArray = []
    i = 0
    splitValue = IP.split('.')
    if len(splitValue) == 4:
        for each in splitValue:
            if each == "":
                i = 1
                break
            if len(each) > 1:
                if each[0] == "0":
                    i = 1
                    break
            if each.isdigit():
                castedVal = int(each)
            else:
                i = 1
                break
            if castedVal < 0 or castedVal > 255:
                i = 1
        if i == 0:
            finalArray.append("IPv4")
    elif len(IP.split(':')) == 8:
        splitValue = IP.split(':')
        if len(splitValue) == 8:
            for each_array in splitValue:
                if each_array == "":
                    i = 1
                    break
                if len(each_array) > 4:
                    i = 1
                    break
                for eachChar in each_array:
                    if not (48 <= ord(eachChar) <= 57 or 97 <= ord(eachChar) <= 102 or 65 <= ord(eachChar) <= 70):
                        i = 1
                        break
            if i == 0:
                finalArray.append("IPv6")
    else:
        i = 1
    if i == 1:
        finalArray.append("Neither")
    return finalArray[0]