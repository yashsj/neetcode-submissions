class Solution {
    public int[] sortArray(int[] nums) {
        int l=0;
        int h=nums.length-1;
        mergesort(nums,l,h);
        return nums;
    }
    public void mergesort(int[] nums, int l, int h){
        if(l>=h)return;
         
        int mid=l+(h-l)/2;
        mergesort(nums,l,mid);
        mergesort(nums,mid+1,h);
        merge(nums,l,mid,h);
    }
    public void merge(int[] nums,int l,int mid,int h){
        int i=l;
        int j=mid+1;
        //int k=0;
        ArrayList<Integer> list = new ArrayList<>();
        while(i<=mid && j<=h){
            if(nums[i]<nums[j]){
                list.add(nums[i]);
                i++;
            }
            else{
                list.add(nums[j]);
                j++;
            }
        }
        while(i<=mid){
            list.add(nums[i]);
            i++;
        }
        while(j<=h){
            list.add(nums[j]);
            j++;
        }
        //nums=list.stream().mapToInt(Integer::intValue).toArray();-->new array created but chnages should happend in place
        int m=0;
        for(int k=l;k<=h;k++,m++)
            nums[k]=list.get(m);
            
 

    }
}