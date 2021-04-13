'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
'''


def findMedianSortedArrays(nums1, nums2):
    full = sorted(nums1 + nums2)
    middle = len(full) // 2
    # if odd, return middle number
    if len(full) % 2 !=0:
        return full[middle]
    # if even, sum middle two and dvidie
    elif len(full) % 2 == 0:
        adders = (full[middle] + full[middle - 1])
        return adders / 2




l1 = [1,2]
l2 = [3,4]

print(findMedianSortedArrays(l1, l2))
