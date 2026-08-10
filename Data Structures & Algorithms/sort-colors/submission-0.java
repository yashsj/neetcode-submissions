class Solution {
    public void sortColors(int[] nums) {
        int n=nums.length;
        int left=0;
        int right=n-1;
        int i=0;
        while(i<=right){
            if(nums[i]==0){
                int a=nums[left];
                nums[left]=nums[i];
                nums[i]=a;
                left++;
                i++;
            }
            else if(nums[i]==2){
                int a=nums[right];
                nums[right]=nums[i];
                nums[i]=a;
                right--;
            }
            else{
                i++;
            }
        }
    }
}