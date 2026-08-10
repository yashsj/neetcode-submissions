class Solution {
    public int maxProfit(int[] prices) {
       int n=prices.length;
        if(n==1)return 0;
        int result=0;
        int i=0,j=1;
        int prev=0;
        while(j<n){
            if(prices[j]<prices[i]){
                i=j;
 //               j++;
            }
            else{
                
                while(j<n && prices[j]>=prev){
                    prev=prices[j];
                    j++;
                }
 //               int d=prev-prices[i];
                result+=(prev-prices[i]);
                i=j;
 //               j++;
                prev=0;

            }
            j++;
        }
    return result;
    }
}