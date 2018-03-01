class Solution:
    def simplifyPath(self, path):
        path=path.split('/')
        stk=[]
        simplePath=""
        stk=stk[1:len(stk)-2]
        for each in path:
            if each != '':
                if each=='.' or each =='/':
                    pass
                elif each=='..':
                    if len(stk) !=0:
                        stk.pop()
                    else:
                        stk.append('')
                else:
                    stk.append(each)
        if len(stk)==0:
            simplePath+='/'
        for each in stk:
            if each != '':
               simplePath+='/'
               simplePath+=each

        return(simplePath)



S=Solution()
print(S.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"))