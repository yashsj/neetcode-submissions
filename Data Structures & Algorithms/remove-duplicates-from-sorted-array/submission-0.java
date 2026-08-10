class Solution {
    public int removeDuplicates(int[] nums) {
        int left=0;
        int right=0;
        int n=nums.length;
        int last=nums[0];
        while(right<n){
            if(nums[right]!=last){
                nums[++left]=nums[right];
                last=nums[right];
            }
            right++;
        }
        return left+1;
    }
}