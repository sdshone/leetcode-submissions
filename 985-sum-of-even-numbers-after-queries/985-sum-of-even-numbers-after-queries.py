class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        
        curr_sum = sum([n for n in nums if n %2 == 0])
        print(curr_sum)
        res = []
        for num, idx in queries:
            print(num, idx)
            if nums[idx]%2 == 0:
                
                if num %2 ==0:
                    curr_sum += num         
                else:
                    curr_sum -= nums[idx]
                
            else:
                if num %2 != 0:

                    curr_sum += nums[idx]
                    curr_sum += num
            nums[idx] += num
            res.append(curr_sum)
            # print(res)
        
        return res