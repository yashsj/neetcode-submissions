class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> map= new HashMap<>();
        List<List<String>> ans = new ArrayList<>();
        for(int i=0;i<strs.length;i++){
            String str=strs[i];
            int[] a=new int[26];
            for(char c : str.toCharArray())
            {
                a[c-'a']++;
            }
            String s=Arrays.toString(a);
            if(!map.containsKey(s)){
                map.put(s,new ArrayList<>());
            }
            map.get(s).add(str);
        }

        for(String k:map.keySet()){
            ans.add(map.get(k));
        }
    return ans;
    }
}
