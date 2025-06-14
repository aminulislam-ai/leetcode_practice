class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_val = num
        min_val = num
        
        for d1 in set(s):
            for d2 in "0123456789":
                if d1 == d2:
                    continue
                remapped = s.replace(d1, d2)
                remapped_val = int(remapped)
                max_val = max(max_val, remapped_val)
                min_val = min(min_val, remapped_val)
        
        return max_val - min_val