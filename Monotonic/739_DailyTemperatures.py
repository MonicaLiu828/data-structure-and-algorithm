class Solution:
# stack to store temperatures
# iterate temp if > stack pop and then push, else stack push directly
#  if pop, popped item index is minus buy new item index put result as answer for popped item

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        answer = [0]* len(temperatures)
        for count,temp in enumerate(temperatures):
            if not stack:
                stack.append(count)
            else:
                while stack and temp > temperatures[stack[-1]]:
                    answer[stack[-1]]= count - stack[-1]
                    stack.pop()
                stack.append(count)
        return answer

# time : O(n)
# space: O(n)
