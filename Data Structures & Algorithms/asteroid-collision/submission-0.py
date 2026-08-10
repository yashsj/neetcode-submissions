class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        stack=[]
        i=0
        for a in asteroids:
            curr=a
            if curr>0:
                stack.append(curr)
            else:
                if stack and stack[-1]>0:
                    while stack and stack[-1]>=0 and stack[-1]<abs(curr):
                            stack.pop()
                if not stack : stack.append(curr)
                elif stack[-1]==abs(curr): stack.pop()
                elif stack and stack[-1]<0:
                    stack.append(curr)
                
        while stack:
            ans.insert(0,stack.pop())

        return ans
    