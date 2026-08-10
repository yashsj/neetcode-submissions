class Solution {
    public int[] topKFrequent(int[] nums, int k) {
       // If we use Priority queue the time complexity goes to O(nlogn)
       //Bucket sort time O(N) and space O(N)
       HashMap<Integer,Integer> frequency = new HashMap<>();
       for(int n:nums){
            frequency.put(n,frequency.getOrDefault(n,0)+1);
       }
       int n=nums.length;
       //int[] bucket = new int[];
       List<Integer>[] bucket = new List[n+1];
       for(int i=0;i<=n;i++){
            bucket[i]= new ArrayList<>();
    }
       for(int key:frequency.keySet()){
            //List<Integer> list = bucket[frequency.get(key)]
            bucket[frequency.get(key)].add(key);
       }
       List<Integer> ans = new ArrayList<>();
       int j=n;
       //int i=k;
       while(k>0){
            List<Integer> l=bucket[j];
            j--;
            if(l.size()==0){
                continue; 
                }
            ans.addAll(l);
            k=k-l.size();
       }
    return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}