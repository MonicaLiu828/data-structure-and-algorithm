# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         # // return set of all permutation for str
#         if len(s1) > len(s2):
#             return False
#         stor1 = defaultdict(int)
#
#         for item in s1:
#             stor1[item] += 1
#
#         def compare(stor1, stor2):
#             for key in stor1:
#                 if key not in stor2:
#                     return False
#                 if stor1[key] != stor2[key]:
#                     return False
#             return True
#
#         i, j = 0, 0
#         stor2 = defaultdict(int)
#         while j < len(s1):
#             stor2[s2[j]] += 1
#             j += 1
#         #  why j needs to = len(s2), like dcb, adcb, when enter in this while loop
#         #  j is in b , adc not equal to dcb, stor2 add b into stor, i moves to d
#         #  j += 1 j equals to len(s2), it will not go into this while loop, that's why
#         # we need j <= len(s2)
#         #  this will also judge when stor1 length == stor2 length, it will go into line
#         #  32 compare directly
#         while j <= len(s2):
#             if compare(stor1, stor2):
#                 return True
#             #  since at this moment, j is out of range, if at this moment stor1 != stor2,
#             #  we can return false directly
#             if j == len(s2):
#                 return False
#             stor2[s2[j]] += 1
#             stor2[s2[i]] -= 1
#             i += 1
#             j += 1
#         return False
#
#
#
#
#
# txt = "12345"
# x = txt.split(' ')
# print(x)