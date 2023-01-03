# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
# or false otherwise.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        stor = set(sentence)
        if len(stor) == 26:
            return True
        return False