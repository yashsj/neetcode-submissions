class MyHashSet {
    List<List<Integer>> list;
    public MyHashSet() {
         list = new LinkedList<>();
         for(int i=0;i<100;i++){
            list.add(null);
         }
    }
    
    public void add(int key) {
        int hash=key%100;
        if(list.get(hash)==null){
            list.set(hash,new LinkedList<>());
            list.get(hash).add(key);
        }
        else{
            List<Integer> l=list.get(hash);
            if(!l.contains(key))l.add(key);
        }
    }
    
    public void remove(int key) {
        int hash=key%100;
        List<Integer> l=list.get(hash);
        if(l!=null&&l.contains(key))
        {
            l.remove(Integer.valueOf(key));
        }
    }
    
    public boolean contains(int key) {
        int hash=key%100;
        List<Integer> l=list.get(hash);
        if(l!=null)return l.contains(key);
        return false;
    }
}
//HashSet and HashMap in Java are both implemented using a hash table internally.
/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */