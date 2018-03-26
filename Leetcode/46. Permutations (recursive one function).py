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

class Solution(object):  

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            
            return [[]]
        
        else:
        
            elm = nums.pop()
        
            nums_vect_new = []

            for vect in self.permute(nums):

                for i in range(len(vect) + 1):

                    nums_temp = vect.copy()
                    nums_temp.insert(i, elm)
                    nums_vect_new.append(nums_temp)

            return nums_vect_new
