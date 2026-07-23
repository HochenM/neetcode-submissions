class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl=[]
        tl=[]
        for i in s:
            sl.append(i)

        for j in t:
            tl.append(j)

        sl.sort(), tl.sort()
        if sl ==tl:

            return True
        return False


        