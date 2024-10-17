class Solution:
    def maximumSwap(self, num: int) -> int:
        
        digits = list(str(num))
        n = len(digits)

        max_idx = [0] * n
        max_idx[-1] = n - 1

        for i in range(n-2, -1, -1):
            if digits[i] > digits[max_idx[i + 1]]:
                max_idx[i] = i
            else:
                max_idx[i] = max_idx[i+1]
        
        for i in range(n):
            if digits[i] != digits[max_idx[i]]:
                digits[i], digits[max_idx[i]] = digits[max_idx[i]], digits[i]
                break

        return int(''.join(digits))