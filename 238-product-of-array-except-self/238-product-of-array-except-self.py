class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p=1
        
        # 왼쪽곱샘
        for i in range(0, len( nums)) : 
            out.append(p)
            p = p * nums[i]
        p=1
                         
        # 왼쪽곱셈결과에오른쪽값을차례대로곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
            
        return out