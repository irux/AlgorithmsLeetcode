"""
This solution has the following results:

Runtime: 40 ms, faster than 87.35% of Python3 online submissions for Two Sum.
Memory Usage: 14.7 MB, less than 5.08% of Python3 online submissions for Two Sum.

03/05/2019
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        where_to_find = {}
        for index,  num in enumerate(nums):
            if num in where_to_find:
                my_partner = where_to_find[num]
                return [my_partner,index]
            else:
                searched = target-num
                where_to_find[searched] = index