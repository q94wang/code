'''
16. Permutations II
Given a list of numbers with duplicate number in it. Find all unique permutations.
Example
For numbers [1,2,2] the unique permutations are:

[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
'''

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        
        if len(nums) == 0:
            
            return [[]]
        
        else:
        
            elm = nums.pop()
        
            nums_vect_new = []

            for vect in self.permuteUnique(nums):

                for i in range(len(vect) + 1):

                    nums_temp = vect.copy()
                    nums_temp.insert(i, elm)
                    
                    if nums_temp not in nums_vect_new:
                        nums_vect_new.append(nums_temp)

            return nums_vect_new