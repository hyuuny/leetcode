class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = {}
        count = 0
        
        # 돌(S)의 빈도 수 계산
        for char in S:
            # 처음이면 1 저장
            if char not in freqs:
                freqs[char] = 1
            else:
            # 이미 있으면 +1
                freqs[char] += 1
        
        # 보석(J)의 빈도 수 합산
        for char in J:
            if char in freqs:
                count += freqs[char]
        
        return count