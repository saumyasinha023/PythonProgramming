class Solution(object):
    def validIPAddress(self, IP):
        if '.' in IP:

            varIP4 = IP.split('.')
            for each in varIP4:
                each = int(each)
                if each > 255 or str(each)[0] == 0:
                    break
                else:
                    print("IPv4")
        elif ':' in IP:
            varIP6 = IP.split(':')



S = Solution()
S.validIPAddress("256.256.256.256")
