class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(sub_list, idx):
            list_len = len(sub_list)
            if not sub_list: return -1
            mid = list_len // 2

            if sub_list[mid] > target:
                return binary_search(sub_list[:mid], idx)
            elif sub_list[mid] < target:
                return binary_search(sub_list[mid+1:], mid+1+idx)
            else:
                return mid+idx
        return binary_search(nums, 0)