"""Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(2,c):
            if i*i >= c:
                break
            count = 0
            if c%i == 0:
                while c%i == 0:
                    count += 1 
                    c/=i
                if i%4 == 3 and count%2 != 0:
                    return False
        return c%4 != 3
        



s = Solution()
print(s.judgeSquareSum(c=5))