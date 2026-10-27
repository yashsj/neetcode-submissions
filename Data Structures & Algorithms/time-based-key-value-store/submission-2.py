class TimeMap:

    def __init__(self):
        self.hashmap={}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key]=[]
        self.hashmap[key].append((timestamp,value))


        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        arr=self.hashmap[key]
        left=0
        res=""
        right=len(arr)-1
        if timestamp<arr[0][0]:
            return ""
        
        while left<=right:
            mid=(left+right)//2
            if arr[mid][0]<=timestamp:
                res=arr[mid][1]
                left=mid+1
            else:
                right=mid-1
            """ if arr[mid][0]==timestamp:
                return str(arr[mid][1])
            elif arr[mid][0]<timestamp:
                left=mid+1

            else: 
                right=mid-1
        return "" if timestamp<arr[0][0] else str(arr[left][1])"""
        return res
                
            

        
