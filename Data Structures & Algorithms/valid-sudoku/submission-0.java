class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> set = new HashSet<>();
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                char n=board[i][j];
                if(n!='.'){
                    // if(!set.add(n+"belongs to col:"+j)||!set.add(n+"belongs to row:"+i)
                    // ||!set.add("belongs to sqr:"+i/3+" "+j/3)){
                    //     return false;
                    if(!set.add(n+"belongs to col:"+j))return false;
                    if(!set.add(n+"belongs to row:"+i))return false;
                    if(!set.add(n+"belongs to sqr:"+i/3+" "+j/3))return false;
                    }
                }
            }
        
        return true;
    }
}
