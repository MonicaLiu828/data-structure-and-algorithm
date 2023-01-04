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
            if item == '':
                continue
            elif item == '.':
                continue
            elif stack and item == '..':
                stack.pop()
            elif not stack and item == '..':
                continue
            else:
                stack.append(item)
        final_str = '/' + '/'.join(stack)
        return final_str
