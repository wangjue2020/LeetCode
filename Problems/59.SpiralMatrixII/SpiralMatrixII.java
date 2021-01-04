public class SpiralMatrixII {
    public int[][] generateMatrix(int n) {
        int[][] ans = new int[n][n];
        int r = 0;
        int c = 0;
        //1 ->, 2 down, 3 left, 4 up
        int direction = 0;
        for(int i =1; i <= n*n; i++){
            if (r > n-1 || c > n-1 || r<0 ||c< 0||ans[r][c] !=0 ) {
                direction = (++direction) % 4;
                int[] newInd = moveIndex(r,c,true, direction);
                r = newInd[0];
                c = newInd[1];
            }
            if(ans[r][c] == 0){
                ans[r][c] = i;
            }
            int[] newInd = moveIndex(r,c,false, direction);
            r = newInd[0];
            c = newInd[1];
        }
        return ans;
    }

    /**
     * compute the next available position for filling the two-dimensional array
     * @param r
     * @param c
     * @param outOfIndex
     * @param direction
     * @return
     */
    public int[] moveIndex(int r, int c, boolean outOfIndex, int direction){
        switch(direction){
            case 0:
                c++;
                if(outOfIndex)
                    r++;
                break;
            case 1:
                r++;
                if(outOfIndex)
                    c--;
                break;
            case 2:
                c--;
                if(outOfIndex)
                    r--;
                break;
            case 3:
                r--;
                if(outOfIndex)
                    c++;
                break;
        }
        return new int[]{r,c};
    }
}
