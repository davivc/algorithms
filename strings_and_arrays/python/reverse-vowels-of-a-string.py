class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e','i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowelsStr = []
        vowelsPos = []
        splitS = [*s]

        for i in range(len(s)):
            if s[i] in vowels:
                vowelsStr.append(s[i])
                vowelsPos.append(i)

        for i in range(len(vowelsStr)):
            pos = vowelsPos[i]
            splitS[pos] = vowelsStr[len(vowelsStr)-i-1]

        return ''.join(splitS)