class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num=0
        for i in range(32):
            reversed_num=reversed_num<<1
            bit=n&1
            reversed_num=reversed_num| bit
            n=n>>1
        return reversed_num
