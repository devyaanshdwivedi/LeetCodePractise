class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        cnt1 = 0
        cnt2 = 0
        cnt = 0
        
        while cnt1 < m and cnt2 < n:
            
            if nums1[cnt] > nums2[cnt2]:
                for i in range(m + n - 1, cnt, -1):
                    nums1[i] = nums1[i - 1]
                nums1[cnt] = nums2[cnt2]

                cnt2 += 1
                cnt += 1
            else:
                cnt1 += 1
                cnt += 1
        
        while cnt2 < n:
            
            for i in range(m + n - 1, cnt, -1):
                nums1[i] = nums1[i - 1]
            nums1[cnt] = nums2[cnt2]
            cnt2 += 1
            cnt += 1


            
        """
        Do not return anything, modify nums1 in-place instead.
        """
        