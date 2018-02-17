def countAndSay(string):
    if len(string)<=1:
        return string
    else:
        count=1
        pointer=0
        arr=[]
        for each in range(1, len(string)):
            if string[each]==string[pointer]:
                count += 1
                if each==len(string)-1:
                    arr.append(string[pointer])
                    arr.append(str(count))
            else:
                if each == len(string) - 1:
                    arr.append(string[pointer])
                    if count>1:
                        arr.append(str(count))
                    arr.append(string[each])
                else:
                    if count>1:
                        arr.append(string[pointer])
                        arr.append(str(count))
                        count=1
                        pointer=each
                    else:
                        arr.append(string[pointer])
                        count=1
                        pointer=each

    return "".join(arr)

print(countAndSay("ABAABBBC"))