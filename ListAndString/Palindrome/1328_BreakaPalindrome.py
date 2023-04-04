class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        palindrome = list(palindrome)
        print(palindrome)
        if len(palindrome) == 1:
            return ''
        flip = False
        for i in range(len(palindrome)):
            char = palindrome[i]
            if char != 'a' and len(palindrome) % 2 == 0:
                palindrome[i] = 'a'
                flip = True
                break
            if char != 'a' and len(palindrome) % 2 == 1 and i != (len(palindrome) - 1) / 2:
                palindrome[i] = 'a'
                flip = True
                break
        if flip == False:
            palindrome[-1] = 'b'
        return ''.join(palindrome)
