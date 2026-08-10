class Solution {
    public int firstMissingPositive(int[] nums) {
        int len=nums.length;
        int res=1;
        for(int i=0;i<len;i++){
            if(nums[i]<0){
                nums[i]=0;
            }
        }
        for(int i=0;i<len;i++){
            int val=Math.abs(nums[i]);
            int index=val-1;
            if(index>=0&&index<len)
            {   
                if(nums[index]>0)nums[index]=nums[index]*-1;
                else if(nums[index]==0) nums[index]=(len+1)*-1;
            }
        }

        for(int i=0;i<len;i++){
            if(nums[i]>=0)
            {
                //res=i+1;
                return i+1;
                //break;
            }
        }
    return len+1;
    }
}