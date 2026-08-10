class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> list = new ArrayList<>();
        int n=nums.length;
        for(int i=0;i<n-2;i++){
            int sum=nums[i]*-1;
            int j=i+1;
            int k=n-1;
            if(i==0||nums[i]!=nums[i-1]){
                while(j<k){
                    if(nums[j]+nums[k]==sum){
                        //list.add(new ArrayList<>());
                        list.add(Arrays.asList(nums[i],nums[j],nums[k]));

                        while(j<k&&nums[j]==nums[j+1])j++;
                        while(j<k&&nums[k]==nums[k-1])k--;
                        j++;
                        k--;
                    }
                    else if(nums[j]+nums[k]>sum){
                        k--;
                    }
                    else{
                        j++;
                    }
                }
            }
        }
        return list;

    }
}

//TC:O(N^2)
//SC:O(logn)or O(N)