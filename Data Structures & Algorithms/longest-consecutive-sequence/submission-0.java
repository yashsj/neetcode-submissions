class Solution {
    public int longestConsecutive(int[] nums) {
        int max=0;
        HashSet<Integer> set = new HashSet<>();
        for(int n:nums){
            set.add(n);
        }

        for(int i=0;i<nums.length;i++){
            int n=nums[i];
            int count=0;
            if(set.contains(n-1))continue;
            while(set.contains(n))
                {
                    count++;
                    n=n+1;
                }
            max=Math.max(count,max);
            }
        return max;
        }
    
}
