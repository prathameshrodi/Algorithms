from typing import List
from itertools import accumulate


class Solution:
    def totalStrength_1(self, strength: List[int]) -> int:
        total_strength = 0
        mod = 10 ** 9 + 7

        def calc_total(n, total_strength):
            for i in range(len(strength) + 1 - n):
                print(min(strength[i:i + n]) * sum(strength[i:i + n]))
                total_strength = total_strength + (min(strength[i:i + n]) * sum(strength[i:i + n]))
            return total_strength

        for i in range(1, len(strength) + 1):
            total_strength = calc_total(i, total_strength)
        return total_strength % mod

    def totalStrength_2(self, A):
        mod = 10 ** 9 + 7
        n = len(A)

        right = [n] * n
        left = [-1] * n
        st = []
        for i in range(n):
            if st:
                a_st = A[st[-1]]
                a_i = A[i]
            while st and A[st[-1]] >= A[i]:
                right[st.pop()] = i
            if st:
                left[i] = st[-1]
            st.append(i)

        res = 0
        acc = list(accumulate(accumulate(A), initial=0))
        for i in range(n):
            l, r = left[i], right[i]
            lacc = acc[i] - acc[max(l, 0)]
            racc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            res += A[i] * (racc * ln - lacc * rn) % mod
        return res % mod


if __name__ == '__main__':
    print(Solution().totalStrength_1([1, 3, 1, 2]))
    print(Solution().totalStrength_2([1, 3, 1, 2]))
