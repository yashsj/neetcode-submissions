class NumMatrix {
    int[][] numMatrix;
    public NumMatrix(int[][] matrix) {
        numMatrix=matrix;
        reintialize();
    }

    public void reintialize(){
        int r=numMatrix.length;
        int c=numMatrix[0].length;
        for(int i=1;i<r;i++){
            numMatrix[i][0]+=numMatrix[i-1][0];
        }
        for(int j=1;j<c;j++){
            numMatrix[0][j]+=numMatrix[0][j-1];
        }
        for(int i=1;i<r;i++){
            for(int j=1;j<c;j++){
                numMatrix[i][j]+=(numMatrix[i][j-1]+numMatrix[i-1][j]-numMatrix[i-1][j-1]);
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        if(row1==0&&col1==0)return numMatrix[row2][col2];
        else if(row1==0) return numMatrix[row2][col2] - numMatrix[row2][col1-1];
        else if(col1==0) return numMatrix[row2][col2] - numMatrix[row1-1][col2];
        else return numMatrix[row2][col2] - numMatrix[row1-1][col2] - numMatrix[row2][col1-1] + numMatrix[row1-1][col1-1];
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */