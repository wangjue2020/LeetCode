class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        addon = 1
        for i in range(len(digits)-1, -1,-1):
            cur_sum = digits[i] + addon
            if cur_sum <10:
                digits[i] = cur_sum
                return digits
            else:
                digits[i] = cur_sum - 10
        return [1]+digits