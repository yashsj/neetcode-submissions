class Solution {
    public int maxArea(int[] heights) {
        int left=0;
        int right=heights.length-1;
        int ans=0;
        int maxleft=0;
        int maxright=0;
        while(left<right){
            if(heights[left]<heights[right]){
                if(heights[left]>maxleft){
                    maxleft=heights[left];
                    ans=Math.max(ans,(right-left)*maxleft);
                }
                left++;
            }
            else{
                if(heights[right]>maxright){
                    maxright=heights[right];
                    ans=Math.max(ans,(right-left)*maxright);
                }
                right--;

            }
        }
        return ans;  
    }
}
