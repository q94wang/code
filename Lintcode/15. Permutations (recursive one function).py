'''
15. Permutations

Given a list of numbers, return all possible permutations.

 Notice

You can assume that there is no duplicate numbers in the list.

Example
For nums = [1,2,3], the permutations are:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here

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