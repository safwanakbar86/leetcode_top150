def merge(self, nums1, m, nums2, n):
    x = (m + n) - n
    j = 0
    for i in range(x, (m + n)):
        nums1[i] = nums2[j]
        j += 1
    nums1.sort()
