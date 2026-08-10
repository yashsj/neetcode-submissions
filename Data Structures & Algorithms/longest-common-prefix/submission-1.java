class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix=strs[0];
        for(String s:strs){
            if(s.startsWith(prefix))continue;
            else{
                int l=prefix.length();
                while(l>=0&&!s.startsWith(prefix)){
                    prefix=prefix.substring(0,l);
                    l--;
                }
        }
        }
    return prefix;
    }
}




//Time C - O(N*m)
//Space C - O(1)