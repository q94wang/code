'''
46. Permutations

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''

import copy

class Solution(object):
    
    def permute_onestep(self, nums_vect_old, new_number):

        if nums_vect_old is None:

            return [[new_number]]

        nums_vect_new = []

        for vect in nums_vect_old:

            for i in range(len(vect) + 1):

                nums_temp = copy.copy(vect)
                nums_temp.insert(i, new_number)
                nums_vect_new.append(nums_temp)

        return nums_vect_new    
    
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) != 0:
        
#             elm = nums[-1]
#             nums_short = nums[:-1]

#             return permute_onestep(permute(nums_short), elm)
        
            elm = nums.pop()
        
            return self.permute_onestep(self.permute(nums), elm)