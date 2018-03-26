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

    def permute_onestep(self, nums_vect_old, new_number):

        # if len(nums_vect_old) == 0:

        #     return [[new_number]]

        nums_vect_new = []

        for vect in nums_vect_old:

            for i in range(len(vect) + 1):

                nums_temp = vect.copy()
                nums_temp.insert(i, new_number)
                nums_vect_new.append(nums_temp)

        return nums_vect_new 
    
    def permute(self, nums):
        # write your code here

        if len(nums) != 0:
        
#             elm = nums[-1]
#             nums_short = nums[:-1]

#             return permute_onestep(permute(nums_short), elm)
        
            elm = nums.pop()
        
            return self.permute_onestep(self.permute(nums), elm)
        
        return [[]]
