class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        days = []

        for idx, temp in enumerate(temperatures):
            while len(days) > 0 and temp > temperatures[days[-1]]:
                answer[days[-1]] = idx - days[-1]
                days.pop()

            days.append(idx)
       
        return answer
