class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        addon = 1
        for i in range(len(digits)-1, -1,-1):
            addon = digits[i] + addon
            if addon <10:
                digits[i] = addon
                return digits
            else:
                digits[i] = addon - 10
                addon = 1
        return [1]+digits