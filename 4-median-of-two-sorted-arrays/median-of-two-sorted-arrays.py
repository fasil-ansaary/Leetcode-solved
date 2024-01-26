class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i,j=0,0
        flag = True
        numsfinal = []
        while flag:
            if i<len(nums1) and j<len(nums2):
                if nums1[i] < nums2[j]:
                    numsfinal.append(nums1[i])
                    i+=1
                else:
                    numsfinal.append(nums2[j])
                    j+=1
            else:
                flag = False
        while i<len(nums1):
            numsfinal.append(nums1[i])
            i+=1
        while j<len(nums2):
            numsfinal.append(nums2[j])
            j+=1
        mid = len(numsfinal)/2
        if len(numsfinal)%2 == 0:
            median = float(numsfinal[mid-1]+numsfinal[mid])/2
        else:
            median = float(numsfinal[mid])
        return median