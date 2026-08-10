class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> list=new ArrayList<>();
          int a1=-1, c1=0;
          int a2=-1,c2=0;
          int len=nums.length;
          for(int n:nums){
            if(n==a1){
                c1++;
            }
            else if(n==a2){
                c2++;
            }
            else if(c1==0){
                a1=n;
                c1=1;
            }
            else if(c2==0){
                a2=n;
                c2=1;
            }
            else{
                c1--;
                c2--;
            }

          }
          c1=c2=0;
          for(int n:nums){
            if(n==a1)c1++;
            if(n==a2)c2++;
          } 
          if(c1>len/3)list.add(a1);
          if(c2>len/3)list.add(a2);
          return list;
    }
}