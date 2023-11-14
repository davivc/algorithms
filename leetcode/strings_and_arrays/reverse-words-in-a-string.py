class Solution:
    def reverseWords(self, s: str) -> str:
        splitS = s.strip().split(' ')
        output = []
        for i in range(len(splitS)):
            if splitS[i] != "":
                output.append(splitS[i])

        output.reverse()
        return ' '.join(output)
                
            