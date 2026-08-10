class Solution {

    public String encode(List<String> strs) {
        String res="";
        for(int i=0;i<strs.size();i++){
            String s=strs.get(i);
            int n=s.length();
            res=res.concat(String.valueOf(n)).concat("#").concat(s);
        }
        return res;
    }

    public List<String> decode(String str) {
        List<String> list = new ArrayList<>();
        int n=str.length();
        int i=0;
        while(i<n){
            int j=i;
            String num="";
            while(str.charAt(j)!='#'){
                //num=num.concat(String.valueOf(str.charAt(j)));
                num=num+str.charAt(j);
                j++;
            }
            int l=Integer.parseInt(num);
            list.add(str.substring(j+1,j+1+l));
            i=j+1+l;
        }
        return list;

    }
}
//Time Complexity: O(K)
//Space Compelexity: O(N+K)
