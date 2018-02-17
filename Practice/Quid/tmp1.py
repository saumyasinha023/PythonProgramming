def returnCountLeaves(N,arr):
    flagList=[arr[0]]

    for i in range(len(arr)):
        flagVal=False
        for j in range(len(flagList)):
            if(arr[i]%flagList[j]==0):
                flagVal=True
                break

        if not flagVal:
            flagList.append(arr[i])

    remainingLeaves=0
    for i in range(1,N+1):
        for j in range(len(flagList)):
            if(i%flagList[j]==0):
                remainingLeaves+=1
                break

    return N-remainingLeaves


print(returnCountLeaves(100,[2,5]))