class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        total_len = l1+l2
        median_ind = total_len//2 
        sorted_list = []
        p1 = 0
        p2 = 0
        while p1 < l1 and p2 < l2 and len(sorted_list) <= median_ind:
            if nums1[p1] <= nums2[p2]:
                sorted_list.append(nums1[p1])
                p1 += 1
            elif nums1[p1] == nums2[p2]:
                sorted_list += [nums1[p1], nums1[p1]]
                p1 += 1
                p2 += 1
            else:
                sorted_list.append(nums2[p2])
                p2 += 1
        if len(sorted_list) <= median_ind:
            if p1 < l1:
                sorted_list += nums1[p1:]
            elif p2 < l2:
                sorted_list += nums2[p2:]
        return sorted_list[median_ind] if total_len % 2 == 1 else (sorted_list[median_ind] + sorted_list[median_ind-1]) / 2