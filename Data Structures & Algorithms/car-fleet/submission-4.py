class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        list_car=[]
        for p,s in zip(position,speed):
            list_car.append([p,s])
        
        list_car.sort(key=lambda x:x[0])

        stack=[]
        r=len(list_car)-1
        ans=0
        for p,s in reversed(list_car):
            diff=target-p
            time=diff/s
            while stack and stack[0]<time:
                stack.pop()
                if not stack:
                    ans+=1
                    break
            stack.append(time)

        if stack:
            ans+=1
        return ans
        #TC:O(Nlogn)
        #SC:O(N)
            
            

        