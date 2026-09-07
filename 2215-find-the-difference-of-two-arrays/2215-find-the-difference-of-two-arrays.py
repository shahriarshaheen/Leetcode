class Solution(object):
    def findDifference(self, nums1, nums2):
        set1=set(nums1)
        set2=set(nums2)
        dict_list=[]
        
        list1=[]
        dict_1={}
        for i in range(len(nums1)):
            if nums1[i] not in set2:
                if nums1[i] not in dict_1:
                    list1.append(nums1[i])
                    dict_1[nums1[i]] = 1
        dict_list.append(list1)

        list2=[]
        dict_2={}
        for i in range(len(nums2)):
            if nums2[i] not in set1:
                if nums2[i] not in dict_2:
                    list2.append(nums2[i])
                    dict_2[nums2[i]] = 1
        dict_list.append(list2)
        return dict_list
        