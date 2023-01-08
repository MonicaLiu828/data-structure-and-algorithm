# https://leetcode.com/problems/simplify-path/description/
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_arr = path.split('/')
        for item in path_arr:
            # if item == '':
            #     continue
            # if not stack and item == '..':
            #     stack.append('/')
            # elif stack and stack[-1] == '/' and item != '/':
            #     stack.append('/')
            # else:
            #     stack.append('/')
            #     stack.append(item)
            if item == '' or item == '.' or (not stack and item == '..'):
                continue
            elif stack and item == '..':
                stack.pop()
            else:
                stack.append(item)
        final_str = '/' + '/'.join(stack)
        return final_str

# time: O(n) + O(n) +O(n) => O(3n) => O(n) n is the length of the path
# split path loop(each step takes O(1) for pop/append)

# Space complexity:
# O(n) n is the length of the path. since the stack maximum storing all characters of the path
