class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        avai = m+n-1
        f = m-1
        s = n-1
        while s >-1 and f> -1:
            if nums2[s] >= nums1[f]:
                nums1[avai] = nums2[s]
                avai -=1
                s-=1
            else:
                nums1[avai] = nums1[f]
                avai -= 1
                f-=1
        if f== -1:
            nums1[:avai+1] = nums2[:s+1]