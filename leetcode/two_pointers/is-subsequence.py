class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sList = [*s]
        tList = [*t]

        sList.reverse()
        tList.reverse()

        for i in range(len(sList)):
            if sList[i] not in tList:
                return False

            idx = tList.index(sList[i])
            tList = tList[idx+1:]

        return True 