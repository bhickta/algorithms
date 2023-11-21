#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        total = (len(A) + len(B))
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            m = (l + r)//2
            j = half - m - 2
            
            Aleft = A[m] if m >=0 else float('-infinity')
            Aright = A[m+1] if m+1 < len(A) else float('infinity')
            Bleft = B[j] if j >=0 else float('-infinity')
            Bright = B[j+1] if j + 1 < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright) )/ 2
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1
# @lc code=end

# https://youtu.be/q6IEA26hvXc

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums1.extend(nums2)
    merged = sorted(nums1)
    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
    else:
        return float(merged[n // 2])

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    merged = [0] * (len(nums1) + len(nums2))
    p1, p2, p3 = 0, 0, 0

    while p1 < len(nums1) or p2 < len(nums2):
        v1 = nums1[p1] if p1 < len(nums1) else float('inf')
        v2 = nums2[p2] if p2 < len(nums2) else float('inf')

        if v1 < v2:
            merged[p3] = v1
            p1 += 1
        else:
            merged[p3] = v2
            p2 += 1
        p3 += 1

    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
    else:
        return float(merged[n // 2])
