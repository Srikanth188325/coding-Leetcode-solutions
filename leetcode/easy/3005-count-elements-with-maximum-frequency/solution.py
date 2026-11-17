from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        # Step 1: Count the frequency of each element
        counts = Counter(nums)
        
        # Step 2: Find the maximum frequency
        max_freq = max(counts.values())
        
        # Step 3: Sum the frequencies of elements that match max freq
        return sum(freq for freq in counts.values() if freq == max_freq)
