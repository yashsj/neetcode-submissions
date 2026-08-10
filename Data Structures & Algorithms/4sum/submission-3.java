class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target){
        Arrays.sort(nums);
        List<List<Integer>> list = new ArrayList<>();
        if(nums.length<4) return list;
        int n=nums.length;
        for(int i=0;i<n-3;i++){
            // int sum=nums[i-1]+nums[i];
            // int compliment=target-sum;
            // int j=i+1;
            // int k=n-1;
            if(i==0||nums[i-1]!=nums[i]){
                for(int l=i+1;l<n-2;l++){
                if(l==i+1||nums[l]!=nums[l-1])
            {
                int j=l+1;
                int k=n-1;
                while(j<k){
                    long sum=(long)nums[i]+nums[l]+nums[j]+nums[k];
                    if(sum==target){
                        list.add(Arrays.asList(nums[i],nums[l],nums[j],nums[k]));
                        while(j<k && nums[j]==nums[j+1])j++;
                        while(j<k && nums[k]==nums[k-1])k--;
                        j++;
                        k--;
                    }
                    else if(sum>target){
                        k--;
                    }
                    else{
                        j++;
                    }
                }
            }
            }
            }
        }
        return list;

    }
}